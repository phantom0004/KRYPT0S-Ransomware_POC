<div align="center">

# KRYPT0S : Encrypt, Conceal, Control  
### *Proof-of-Concept Ransomware Wiper*  

<br>

<img src="https://github.com/user-attachments/assets/8f59a03b-5222-41f1-b370-3ed15ef1b735" alt="KRYPT0S Banner" width="600" height="400"/>

<br>

[![Status: PoC](https://img.shields.io/badge/Status-Proof--of--Concept-orange.svg)](#)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](#)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)](#)

</div>

---

## ⚠️ Warning: Legal and Ethical Disclaimer
> **This project is intended solely for educational purposes** and **must be executed only in a controlled, sandboxed environment.**  
>  
> **Unauthorized or real-world use is highly illegal** and may result in **criminal penalties** including imprisonment. The creator of this project disclaims all responsibility for misuse or damages.  
>
> **YOU HAVE BEEN WARNED.**

This repository includes a built-in kill switch to ensure it does not cause irreparable harm. **The goal is NOT to harm** but to facilitate learning about ransomware mechanics—**for academic and cybersecurity research purposes only**.

---

## Project Overview

### About KRYPT0S
**KRYPT0S** is a **Python-based ransomware simulation** crafted to reveal the **inner workings of real-world ransomware**. Its primary objective is to help cybersecurity professionals, researchers, and enthusiasts **understand** ransomware behaviors and **develop** effective defense strategies.

### Key Features
- **Complex Encryption Handling**  
  Utilizes AES encryption to lock files on Windows systems.
- **Persistence and Stealth**  
  Modifies system settings to run in the background and survive reboots.
- **Ransomware Screen**  
  Mimics a WannaCry-style interface (all Bitcoin addresses and data are fake for simulation).
- **Stealth Tactics**  
  Disables Windows Defender, stops security services, and deletes shadow copies.
- **Parallel Encryption**  
  Employs multithreading to encrypt files across all drives quickly.
- **Event Log Removal**  
  Attempts to wipe Windows event logs to conceal its tracks.
- **Vast Encryption Scope**  
  Encrypts various file types—including `.exe` files in critical directories—for maximum disruption.
- **Secure Keys**  
  Generates and protects encryption keys in memory, complicating forensic analysis.
- **Change System Wallpaper**  
  Simulates altering the system wallpaper to instill fear (no actual risk if kill switch is enabled).

---

## Detailed Functionality

### No Decryption Function Present
A **defining characteristic** of KRYPT0S is that there is **no built-in decryption** capability. Once encrypted:
- **File extensions** are changed, complicating recovery efforts.  
- Infections on multiple machines lead to **chaotic** decryption attempts.  
- Victims may be tricked into paying a ransom—but **true recovery is unlikely**.  
- The absence of a decryption routine **underscores** the gravity of ransomware threats and the necessity for strong cybersecurity measures.

### Ransomware Screen
KRYPT0S includes a **fake ransomware screen** for realistic testing scenarios:
- **Fake Bitcoin Details**  
  All addresses and information are fabricated for demonstration only.
- **Simulated Buttons**  
  The user interface is purely illustrative—no real transactions occur.
- **Lockdown Interface**  
  Closes off the “X” button and Alt+F4, making forced termination more challenging.
- **Enhanced Persistence**  
  Continuously rechecks specific registry keys, hindering manual removal attempts.

<div align="center">
  <img src="https://github.com/user-attachments/assets/d3d7814d-7520-484a-b510-c3b9c5ad07c4" alt="Ransomware Screen" width="600" height="500"/>
</div>

---

## Ethical and Safe Usage
KRYPT0S is intended for **academic and training** settings within **sandboxed** environments. A **kill switch** stops its malicious behavior if certain conditions are met, reducing the likelihood of unintentional damage.

### Running the Simulation
1. **Convert and Execute**  
   - Convert the Python scripts (`.py`) into executables (`.exe`) with the provided converter script.  
   - Launch **`KRYPT0S.exe`**; **`Screen.exe`** will run afterward to simulate the ransomware interface.  
2. **Windows Environment Only**  
   - The converter supports **Windows only**. Execution on UNIX-based systems is not supported.

Once running:
- KRYPT0S **scans all drives** and encrypts files with targeted extensions.  
- `.exe` files in crucial directories (like `/Downloads` or `/OneDrive`) are also encrypted, potentially causing a **system meltdown** due to disabled essential programs.  
- This highlights the **catastrophic impact** of true ransomware, emphasizing the importance of strong security measures.

### Kryptos in Action
**Aftermath of the Attack**  
<div align="center">
  <img src="https://github.com/user-attachments/assets/d99e527d-c4dc-4503-b03a-ea3ef7b69a76" alt="Aftermath of the Attack" width="900" height="500"/>
</div>

<br>

**Encrypted Files**  
<div align="center">
  <img src="https://github.com/user-attachments/assets/6d9cd5a8-93a7-4663-af5e-6981fc7fa9b9" alt="Encrypted Files" width="900" height="500"/>
</div>

---

## Conclusion
KRYPT0S is a **powerful educational tool** for illustrating the **complexity and risk** posed by modern ransomware. Properly understanding ransomware behavior is essential for IT professionals and security researchers to build **stronger defenses**. Always use this project under **legal, ethical constraints** and in **isolated** test environments.
