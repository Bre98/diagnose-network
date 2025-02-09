# Network Diagnostics Tool

## Overview
The Network Diagnostics Tool is a Python-based utility designed to automate network troubleshooting tasks such as ping tests, traceroutes, and network interface diagnostics. This tool is compatible with both **Windows** and **Linux** systems, making it a versatile solution for diagnosing connectivity issues.

The tool performs the following tasks:
- **Ping Test**: Sends ICMP packets to a specified host to check connectivity.
- **Traceroute**: Traces the route packets take to reach the specified host.
- **Network Diagnostic**: Displays detailed information about network interfaces (e.g., IP addresses, subnet masks, etc.).

The results of these tests are displayed neatly on the screen for easy interpretation.

## Features
- **Cross-Platform Compatibility**: Works on both Windows and Linux systems.
- **Automated Diagnostics**: Runs ping tests, traceroutes, and network diagnostics in one go.
- **Neatly Organized Results**: Displays results in a clear and structured format for easy understanding.
- **Customizable Host**: Allows users to specify the host (IP address or domain name) to test.

## Prerequisites
- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **Network Tools**: Ensure that `ping`, `traceroute` (Linux) or `tracert` (Windows), and `ifconfig` (Linux) or `ipconfig` (Windows) are available on your system.

## Installation
1. Clone the Repository
 ```
   git clone https://github.com/yourusername/network-diagnostics-tool.git
 ```
2. Navigate to the Project Directory
  ```
cd network-diagnostics-tool
 ```
4. Run the Script
   - Ensure the script has executable permissions (Linux/Mac):
  ```
chmod +x network_diagnostics.py
  ```
   - Run the script:
   ```
python3 network_diagnostics.py <host>
   ```

## Usage
To use the Network Diagnostics Tool, run the script with the following command:
```
python3 network_diagnostics.py <host>
```
- <host>: The IP address or domain name of the host you want to test (e.g., google.com or 8.8.8.8).

### Example
To diagnose connectivity to google.com, run:
```
python3 network_diagnostics.py google.com
```

## Output
The tool will display the results of the following tests:
1. Ping Test: Shows the round-trip time and packet loss.
2. Traceroute: Displays the route packets take to reach the host.
3. Network Diagnostic: Provides details about the network interfaces on your system.

The results are organized neatly for easy interpretation.

## Troubleshooting
- Permission Issues: Ensure you have the necessary permissions to run network diagnostic commands. On Linux, you may need to run the script with sudo.
- Command Not Found: Ensure that ping, traceroute/tracert, and ifconfig/ipconfig are installed on your system.
- Python Not Found: Ensure Python 3.x is installed and accessible from the command line.

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to:
- Open an issue on GitHub.
- Submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
   
