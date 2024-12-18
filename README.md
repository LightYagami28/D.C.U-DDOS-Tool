# D.C.U-DDOS-Tool

**D.C.U-DDOS-Tool** is an IP stress tool with an IP spoofer designed for network testing and stress testing. Please use this tool responsibly and only for ethical purposes.

### Features:
- **IP Spoofing**: Spoof your IP address to disguise the source of traffic.
- **Stress Testing**: Simulate a Distributed Denial of Service (DDoS) attack to test the resilience of networks and services.

---

## Prerequisites

- **Python 3.x** is required to run the tool.
- **Scapy** library for packet crafting and sending.
- **Npcap** or **WinPcap** (on Windows) for packet sniffing (optional, not required for sending packets).

---

## Installation and Setup

### Windows
1. **Install Python 3**:
   - Download and install [Python 3](https://www.python.org/downloads/) from the official website: .
   - Ensure you check the box to add Python to your PATH during installation.

2. **Install Dependencies**:
   Open Command Prompt (CMD) and run the following command:
   ```bash
   pip install scapy
   ```

3. **Install Npcap** (if you want to use sniffing features):
   - Download and install **[Npcap](https://nmap.org/npcap/)**
   - During installation, ensure you select **“Install Npcap in WinPcap API-compatible Mode”**.

4. **Run the Tool**:
   Open CMD and navigate to the directory containing `DCU-DDOS.py`, then execute the following:
   ```bash
   python DCU-DDOS.py
   ```

### Mac OS

1. **Install Python 3**:
   - Mac OS usually comes with Python pre-installed. If not, install Python 3 via [Homebrew](https://brew.sh/)`:
     ```bash
     brew install python
     ```

2. **Install Dependencies**:
   Use `pip3` to install the necessary libraries:
   ```bash
   pip3 install scapy
   ```

3. **Run the Tool**:
   Open the Terminal, navigate to the directory containing `DCU-DDOS.py`, and run:
   ```bash
   python3 DCU-DDOS.py
   ```

4. **Optional: Install Pcap (if sniffing is required)**:
   - Install **libpcap** on Mac OS if you need packet sniffing:
     ```bash
     brew install libpcap
     ```

### Linux

1. **Install Python 3**:
   - On most Linux distributions, Python 3 is already installed. If not, install it using your package manager:
     ```bash
     sudo apt-get install python3
     ```

2. **Install Dependencies**:
   Install **Scapy** and other required libraries:
   ```bash
   sudo apt-get install python3-pip
   pip3 install scapy
   ```

3. **Install Pcap (for sniffing, optional)**:
   Install **libpcap-dev** to enable packet capture:
   ```bash
   sudo apt-get install libpcap-dev
   ```

4. **Run the Tool**:
   Navigate to the directory containing `DCU-DDOS.py` and run the script:
   ```bash
   python3 DCU-DDOS.py
   ```

---

## How to Use

1. **Enter Your Spoofed IP**: This is the IP address that will appear as the source of the attack.
2. **Enter the Target IP**: The IP address of the server or network you wish to stress test.
3. **Enter the Port**: Choose the port that the attack will target (default is port 80 for HTTP traffic).

The script will start sending packets to the target and log the results.

---

## Disclaimer

This tool is intended for **educational purposes** and **network stress testing** in **controlled environments**. **Unauthorized use** of this tool for attacking networks or services without permission is **illegal** and **unethical**. Use this tool responsibly.