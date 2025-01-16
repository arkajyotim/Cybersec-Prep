# Python Port Scanner

This repository contains a simple yet effective Python script for scanning open ports on target systems. The script supports single and multiple target IPs and provides a concise report of open ports.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
    - [Setup](#setup)
    - [Running the Script](#running-the-script)
5. [How It Works](#how-it-works)
6. [Disclaimer](#disclaimer)

---

## Introduction
This Python script is designed to scan a specified number of ports on one or more target IPs. It uses socket programming to identify open ports, making it a useful tool for network analysis and reconnaissance.

---

## Features
- **Multi-Target Scanning:** Scan one or multiple IP addresses by providing them as input.
- **Port Range Selection:** Specify the number of ports to scan (up to 65,535).
- **Open Port Detection:** Identifies and lists all open ports for the target(s).
- **User-Friendly Interface:** Simple input prompts for IPs and port range.

---

## Requirements
- **Python:** Python 3.x installed on your system.
- **Network Access:** Ensure the script can reach the target IP(s) over the network.

---

## Usage

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/PortScanner.git
   cd PortScanner
Install any necessary dependencies (if applicable):

bash
Copy
pip install -r requirements.txt
(Note: No additional libraries are required for this script.)

Running the Script
Execute the script:

bash
Copy
python3 port_scanner.py
Provide input as prompted:

Enter one or more target IP addresses, separated by commas (e.g., 192.168.1.1,192.168.1.2).
Enter the number of ports to scan (e.g., 1000).
View the output:

Open ports are displayed in the terminal for each target.
How It Works
Input Handling:

The script accepts single or multiple target IPs and a port range as input.
Port Scanning:

For each IP address, the script creates a socket connection to each port within the specified range.
If the connection is successful, the port is marked as open.
Output:

Open ports for each target IP are listed in the terminal.
Disclaimer
This script is for educational purposes only. Unauthorized scanning of systems is illegal and unethical. Ensure you have explicit permission before scanning any system.

Feel free to fork, contribute, or raise issues.
Made with ❤️ by JEET