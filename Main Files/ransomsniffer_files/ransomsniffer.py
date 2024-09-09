import time
import os
try:
    from malware_detection import yara_rules
    from malware_detection import pe_analysis
    from malware_detection import virus_total
except ModuleNotFoundError:
    exit("Custom modules not found. Please ensure you have the 'yara_rules.py', 'pe_analysis.py' and 'virus_total.py'!")
try:
    import yara
    import pefile
except ModuleNotFoundError:
    exit("Yara and/or pefile not found! Please ensure you download all dependancies from the 'requirements.txt' file")

# Program Intro Banner
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

# Banner when scanning
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

# Redirects user to another menu based on choice
def menu_switch(choice):
    print(f"Redirecting you to choice {choice} ...")
    time.sleep(1)
    
    os.system("cls") if os.name == "nt" else os.system("clear")
    scan_banner()

# Start virus total scan using module
def virus_total_scan():    
    API_KEY = input("Enter your VirusTotal API key > ").strip()
    data, choice = virus_total_user_arguments()

    # Create the VirusTotalAPI object without client_obj initially
    virus_total_object = virus_total.VirusTotalAPI(choice, data, API_KEY)
    # Connect to VirusTotal API and get the client_object
    client_object, _ = virus_total_object.connect_to_endpoint()
    # Set the client_obj attribute within the same object
    virus_total_object.client_obj = client_object
    
    api_request_string = virus_total_object.craft_api_request()
    output, function_status = virus_total_object.send_api_request_using_vt(api_request_string)

    # Parse output, and see if it was a success
    if function_status == "api_fail":
        print(virus_total_object.parse_API_error(output))
    elif function_status == "general_fail":
        print(output)
    else:
        virus_total_object.parse_API_output(output)

# Handle user input for the virus total API
def virus_total_user_arguments():
    print("\nPlease select what you wish to scan :")
    print("[1] Scan a file \n[2] Scan a URL")
    user_choice = input("Choice > ").strip()
    print()
    
    data = ""
    if user_choice == "1":
        data = input("Enter a file hash or file path to scan > ")
        if "/" in data or "\\" in data or "." in data:
            hash_algo = input("Enter the hashing algorithm to use [md5, sha1, sha256] (Leave blank for sha256) > ").strip().lower()
            data = hash_file(data, hash_algo)
            if not data: 
                exit("[-] File does not exist in system! Please ensure the path is valid")
            else:
                print(f"[+] Successfully hashed file using {hash_algo}. Scanning -> {data}")
    elif user_choice == "2":
        data = input("Enter the URL you wish to scan > ")
    else:
        exit("[-] Invalid Input! Please enter a value between 1 and 2")

    print("\t\t   ------- \n")
    user_choice = "files" if user_choice == "1" else "urls"
    return data, user_choice

# Hash file for virus total scan
def hash_file(path, hash_algo="sha256"):
    virus_total_object = virus_total.VirusTotalAPI()
    
    if not os.path.exists(path):
        return None
    if hash_algo not in ["md5", "sha256", "sha1"]:
        hash_algo = "sha256"
    
    file_data = r""
    with open(path, "rb") as file:
        file_data = file.read()
    
    return virus_total_object.hash_file(file_data, hash_algo)

# Display virus total help menu
def display_API_help():
    print("""
VirusTotal scans files/URLs for threats using multiple antivirus engines. Automate scans via their API.

- Get an API Key:
1. Sign up: https://www.virustotal.com/gui/join-us
2. Go to your profile: https://www.virustotal.com/gui/my-apikey
3. Copy your API key.

- Need Help?
More info: https://virustotal.readme.io/docs/please-give-me-an-api-key

- Resources:
1. Quota: https://virustotal.readme.io/docs/consumption-quotas-handled
2. Public vs Private API: https://virustotal.readme.io/docs/difference-public-private
3. API Overview: https://virustotal.readme.io/docs
    """)

# Enter yara scan menu (still need to implement)
def default_yara_scan():
    pass

# Handle menu user option
def handle_user_arguments():
    try:
        usr_input = input("Choice > ")
    except KeyboardInterrupt:
        exit("[!] Program Exited Successfully")
    if not usr_input or usr_input not in ["1", "2", "3"]:
        exit("Invalid Choice Input - Please ensure your input is in the range of 1-3!")
    
    if usr_input != "3":
        menu_switch(usr_input)
        
    if usr_input == "1":
        virus_total_scan()
    elif usr_input == "2":
        default_yara_scan()
    elif usr_input == "3":
        display_API_help()

# Main function
def main():
    intro_banner()
    handle_user_arguments()

if __name__ == "__main__":
    main()
