#!/usr/bin/env python

import scapy.all as scapy
import argparse

# Printing NetHhunter Banner
def print_banner():
    red = "\033[91m"   # ANSI escape code for bright red
    reset = "\033[0m"    # ANSI escape code to reset color

    banner = f"""
    {red}
             _   _      _   _   _             _            
            | \ | | ___| |_| | | |_   _ _ __ | |_ ___ _ __ 
            |  \| |/ _ \ __| |_| | | | | '_ \| __/ _ \ '__|
            | |\  |  __/ |_|  _  | |_| | | | | ||  __/ |   
            |_| \_|\___|\__|_| |_|\__,_|_| |_|\__\___|_|   
        ====================================================== 

        ======================================================
    {red}
    """
    print(banner + reset)

# parsing the arguments
def get_args():
    parser = argparse.ArgumentParser(description="ARP Scanner Tool")
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range (e.g., 192.168.1.1 or 192.168.1.0/24)", required=True)
    return parser.parse_args()

# Performing scan on the target Ip and parsing results
def scan(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        client_list = []
        for element in answered_list:
            client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
            client_list.append(client_dict)

        return client_list if client_list else None  # Return None if no devices found

    except ValueError:
        return "invalid"  # Return 'invalid' for ValueError
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")
        return None

# printing results
def print_result(results):
    if results == "invalid":
        print("\nERROR: Invalid IP address format. Please provide a valid IP.")
        print("Valid formats include:")
        print(" - A single IP: e.g., 192.168.1.1")
        print(" - A range: e.g., 192.168.1.0/24")
        print(" - A subnet: e.g., 10.0.0.0/8")
    elif results is None:
        print("\nNo devices found.")
    else:
        print("IP Address\t\tMAC Address")
        print("---------------------------------------------------------")
        for client in results:
            print(f"   {client['IP']}\t\t{client['MAC']}")

# main
def main():
    print_banner()
    options = get_args()
    scan_result = scan(options.target)
    print_result(scan_result)


if __name__ == "__main__":
    main()