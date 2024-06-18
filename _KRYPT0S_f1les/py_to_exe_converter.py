import subprocess, os 
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
        print("This will ensure the conversion will work and the .py file will change to a .exe file.")
        
        exit()
        
    print("[✔] Running windows OS \n")
    
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

    print("\nLIBRARY INSTALLATION COMPLETED\n")

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

        print(f"\n[!] Processing the conversion of '{file_name}'. Please stand by, this may take some time.")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
        if result.returncode == 0:
            print(f"[+] File {name} has been converted to {file_name}.exe.")
        else:
            exit(f"[-] A fatal error occurred: {result.stderr}. If this issue persists, try re-installing 'pyinstaller")
        
        clean_pyinstaller_artifacts(file_name)
        
    print("\n[*] Conversion Completed. Please check the 'krytp0s output conversion' folder to view the output")

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
        except:
            print(f"Unable to delete the following directory : {build_dir}")
    
    # Delete __pycache__ directory
    if os.path.exists(pycache_dir):
        try:
            shutil.rmtree(pycache_dir)
        except:
            print(f"Unable to delete the following directory : {pycache_dir}")
    
    # Delete the spec file
    if os.path.exists(spec_file):
        try:
            os.remove(spec_file)
        except:
            print(f"Unable to delete the following directory : {spec_file}")
    
    # Move the executable to the current directory
    if os.path.exists(executable_path):
        try:
            shutil.move(executable_path, new_executable_path)
        except:
            print(f"Unable to move executable file {executable_name} to : {new_executable_path}")
    
    # Delete dist directory
    if os.path.exists(dist_dir):
        try:        
            shutil.rmtree(dist_dir)
        except:
            print(f"Unable to delete the following directory : {dist_dir}")
    
    print(f"[*] Cleanup completed for {executable_name}")
    print() # New line

def banner():
    print("""
         _  ________   _______ ____   ___  ____    ____  _____ _____ _   _ ____  
        | |/ /  _ \ \ / /_   _|  _ \ / _ \/ ___|  / ___|| ____|_   _| | | |  _ \ 
        | ' /| |_) \ V /  | | | |_) | | | \___ \  \___ \|  _|   | | | | | | |_) |
        | . \|  _ < | |   | | |  __/| |_| |___) |  ___) | |___  | | | |_| |  __/ 
     ___|_|\_\_| \_\|_|   |_| |_|    \___/|____/  |____/|_____| |_|  \___/|_|   
        
    """)

banner()    
check_os()

libraries = ["pycryptodome", "requests", "pywin32", "pyinstaller"]
libraries_check_section(libraries)

payload_conversion()