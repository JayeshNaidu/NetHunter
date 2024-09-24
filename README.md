# 👾 NetHunter - Network Scanner Tool 

NetHunter is a simple ARP-based network scanner written in Python using Scapy. It helps identify all the devices connected to a given IP or IP range by broadcasting ARP requests and collecting their IP and MAC addresses. This tool can be useful for basic network diagnostics and security analysis. 

## Features ✨
- 🔍 Scans for devices in a target IP range or a specific IP address
- 🖥️ Displays the IP and MAC addresses of discovered devices
- 🎨 Custom banner for a sleek terminal experience

## Requirements 📋
- Python 3.x 🐍
- Scapy (Python networking library)

## Installation 💻
1. Clone the repository:
   ```bash
   git clone https://github.com/JayeshNaidu/NetHunter.git

## Functions Explanation 🛠️

### 1. `print_banner()`
Prints a stylized NetHunter banner in bright red using ANSI escape codes.

### 2. `get_args()`
Parses the target IP or IP range from the command-line arguments.

### 3. `scan(ip)`
Performs the ARP scan on the specified IP or IP range, returning a list of devices.

### 4. `print_result(results)`
Displays the scan results, including IP and MAC addresses of discovered devices.

### 5. `main()`
Main execution flow that initializes the tool by printing the banner, getting user input, running the scan, and printing the results.


