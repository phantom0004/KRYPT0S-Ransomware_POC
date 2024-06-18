import subprocess, os
import re
import time 
import shutil

def parse_pip_output(pip_output, library_name):
    if "Successfully installed" in pip_output:
        return f"[+] Successfully installed {library_name}!"
    elif "Requirement already satisfied" in pip_output:
        return f"[!] Library {library_name} already installed."
    elif "Defaulting to user installation because normal site-packages is not writeable" in pip_output:
        return f"[!] {library_name} installed in user site-packages due to permission issues."
    else:
        return f"[-] Unable to parse PIP output for {library_name}. The below snippet log was captured : {pip_output[:40]}"
    
def download_library(libraries):
    print("[*] Checking and downloading required PIP libraries")
    for library in libraries:
        command = ["pip", "install", library]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stdout or result.stderr: 
                output = parse_pip_output(result.stdout, library)
                print(output)
            else:
                print(f"No output available for {library}.")
        except Exception as err:
            print(f"[-] Unable to install {library}! Error: {err}. Skipping...")
            
def libraries_check_section(libraries):
    print("PIP LIBRARY INSTALLATION - Downloading required libraries . . . \n")

    download_library(libraries)

    print("\nLIBRARY INSTALLATION COMPLETED")

libraries = ["pycryptodome", "requests", "pywin32"]
libraries_check_section(libraries)