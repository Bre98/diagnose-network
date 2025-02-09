import os
import platform
import subprocess
import sys
from datetime import datetime

# Function to perform a ping test
def ping_test(host):
    print(f"Performing ping test on {host}...")
    try:
        # Determine the ping command based on the OS
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "4", host]  # Send 4 packets for the ping test

        # Run the ping command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("Ping Test Results:")
            print(result.stdout)
        else:
            print(f"Ping test failed: {result.stderr}")
    except Exception as e:
        print(f"Error during ping test: {e}")

# Function to perform a traceroute
def traceroute(host):
    print(f"Performing traceroute to {host}...")
    try:
        # Determine the traceroute command based on the OS
        command = ["tracert", host] if platform.system().lower() == "windows" else ["traceroute", host]

        # Run the traceroute command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("Traceroute Results:")
            print(result.stdout)
        else:
            print(f"Traceroute failed: {result.stderr}")
    except Exception as e:
        print(f"Error during traceroute: {e}")

# Function to perform a network diagnostic (ipconfig/ifconfig)
def network_diagnostic():
    print("Performing network diagnostic...")
    try:
        # Determine the command based on the OS
        command = ["ipconfig", "/all"] if platform.system().lower() == "windows" else ["ifconfig"]

        # Run the network diagnostic command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("Network Diagnostic Results:")
            print(result.stdout)
        else:
            print(f"Network diagnostic failed: {result.stderr}")
    except Exception as e:
        print(f"Error during network diagnostic: {e}")

# Function to display the results neatly
def display_results(results):
    print("\n" + "="*50)
    print("Network Diagnostics Summary")
    print("="*50)
    for key, value in results.items():
        print(f"\n{key}:\n{value}")
    print("="*50 + "\n")

# Main function to run the diagnostics
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 network_diagnostics.py <host>")
        sys.exit(1)

    host = sys.argv[1]
    results = {}

    # Perform the ping test
    ping_output = ping_test(host)
    results["Ping Test"] = ping_output

    # Perform the traceroute
    traceroute_output = traceroute(host)
    results["Traceroute"] = traceroute_output

    # Perform the network diagnostic
    network_output = network_diagnostic()
    results["Network Diagnostic"] = network_output

    # Display the results neatly
    display_results(results)

if __name__ == "__main__":
    main()
