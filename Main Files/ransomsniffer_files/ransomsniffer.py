import yara
import pefile
import time
import os
import yara_rules as y_rules

def intro_banner():
    banner = r"""
            .-""-.
           / .--. \
          / /    \ \
          | |    | |
          | |.-""-.|
         ///`.::::.`\
        ||| ::/  \:: ;               - Ransomsniffer -
        ||; ::\__/:: ;   Detect and Defend Before the Threat Begins.
         \\\ '::::' /
          `=':-..-'`
    """
    
    options = """
Please choose an option:

[1] VirusTotal Scan (API Key Required) 
    - Submit a file or hash for a comprehensive scan using VirusTotal's database.

[2] Default Scan (YARA/Pefile)
    - Perform a standard scan using YARA rules and Pefile for quick threat detection.
    
[3] Display API Key Help
    - Display a help menu showing how to sign up for an API key in a few easy steps.
"""
    print(banner+options)

def scan_banner():    
    banner = r"""
______  ___   _   _  _____  ________  ___ _____ _   _ _________________   _____ _____   ___   _   _ 
| ___ \/ _ \ | \ | |/  ___||  _  |  \/  |/  ___| \ | |_   _|  ___|  ___| /  ___/  __ \ / _ \ | \ | |
| |_/ / /_\ \|  \| |\ `--. | | | | .  . |\ `--.|  \| | | | | |_  | |_    \ `--.| /  \// /_\ \|  \| |
|    /|  _  || . ` | `--. \| | | | |\/| | `--. \ . ` | | | |  _| |  _|    `--. \ |    |  _  || . ` |
| |\ \| | | || |\  |/\__/ /\ \_/ / |  | |/\__/ / |\  |_| |_| |   | |     /\__/ / \__/\| | | || |\  |
\_| \_\_| |_/\_| \_/\____/  \___/\_|  |_/\____/\_| \_/\___/\_|   \_|     \____/ \____/\_| |_/\_| \_/
    """
    
    print(banner+"\n")

def menu_switch(choice):
    print(f"Redirecting you to choice {choice} ...")
    time.sleep(1)
    
    os.system("cls") if os.name == "nt" else os.system("clear")
    scan_banner()

def virus_total_scan():
    pass

def display_API_help():
    print("""
- VirusTotal Information: -
VirusTotal is an online service that scans files and URLs using multiple antivirus engines to identify potential threats. By using their API, you can automate scans and get detailed reports on files, URLs, and more.

- To Get a VirusTotal API Key: -
1. Sign up at VirusTotal: https://www.virustotal.com/signup/
2. After logging in, go to your profile and select "API Key."
3. Copy your API key for use in the application.

Simply paste the API key when prompted after selecting option [1] (VirusTotal Scan).
    """)

def default_yara_scan():
    pass

def handle_user_arguments():
    try:
        usr_input = input("Choice > ")
    except KeyboardInterrupt:
        exit("[!] Program Exited Successfully")
    if not usr_input or usr_input not in ["1", "2", "3", "4"]:
        exit("Invalid Choice Input - Please ensure your input is in the range of 1-3!")
    
    if usr_input != "3":
        menu_switch(usr_input)
        
    if usr_input == "1":
        virus_total_scan()
    elif usr_input == "2":
        default_yara_scan()
    elif usr_input == "3":
        display_API_help()

def main():
    intro_banner()
    handle_user_arguments()

if __name__ == "__main__":
    main()
