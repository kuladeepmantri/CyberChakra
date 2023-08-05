import os
import re
import requests
import socket
import time
import threading
import urllib.parse
import logging

def get_public_ip(url):
    # Use the "ipify" service to get the public IP address
    try:
        response = requests.get(f"https://api.ipify.org?format=json&url={url}")
        return response.json()["ip"]
    except Exception as e:
        logging.error(f"Error getting public IP: {e}")
        return None

def scan_ports(ip_address, ports, num_threads=1):
    # Build the "nmap" command
    command = f"nmap -O -T{num_threads} -p{','.join(map(str, ports))} {ip_address}"

    # Run the "nmap" command to scan the ports
    output = os.popen(command).read()

    # Extract the open ports and OS details from the output
    open_ports = []
    os_details = {}
    for line in output.split("\n"):
        match = re.search(r"^(\d+)/tcp\s+open", line)
        if match:
            open_ports.append(int(match.group(1)))
        elif line.startswith("Running: "):
            os_name = line[9:]
            os_details[os_name] = []
        elif line.startswith("OS details: "):
            os_details[os_name].append(line[13:])

    return open_ports, os_details






if __name__ == "__main__":
    # Print the banner
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Print the banner
    print("=" * 80)
    print(" " * 30 + "Port Scanner by Kuladeep Mantri")
    print("=" * 80)

    # Prompt the user to enter a website or an IP address
    address = input("Enter a website or an IP address to scan: ")

    # Parse the input
    if "." in address:
        # The input is an IP address
        ip_address = address
    else:
        # The input is a URL
        ip_address = get_public_ip(address)
        if not ip_address:
            print("Invalid website or IP address.")
            exit(1)

    # Prompt the user for the number of threads
    num_threads_str = input("Enter the number of threads (optional, default=1): ")

    # Convert the number of threads to an integer
    num_threads = int(num_threads_str) if num_threads_str.isdigit() else 1

    # Prompt the user for the port
    port_str = input("Enter the port range to scan (optional, default=top 500 ports): ")

    # Parse the port range
    if port_str:
        # Convert the port range to a list of integers
        ports = [int(x) for x in port_str.split("-")]
    else:
        # Scan the top 500 ports
        ports = range(1, 501)

    # Display the scan animation
    print("Scanning ports...")
    for i in range(100):
        print(f"\r[{'#' * (i+1):100}] {i+1}%", end="")
        time.sleep(0.1)

    # Scan the ports
    open_ports, os_details = scan_ports(ip_address, ports, num_threads)

    if not open_ports:
        print("No open ports found.")
    else:
        print( "Open ports:")
        for port in open_ports:
            port_name = socket.getservbyport(port)
            print(f"  {port} ({port_name})")
        print("OS details:")
        for os_name, os_lines in os_details.items():
            print(f"  {os_name}:")
            for line in os_lines:
                print(f"    {line}")