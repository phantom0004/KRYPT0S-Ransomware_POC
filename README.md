# KRYPT0S : Encrypt, Conceal, Control - Proof Of Concept Project
![krypt0s-high-resolution-logo](https://github.com/user-attachments/assets/dc9fa9d3-0cfc-4bf8-be4c-cae8dbcc75ba)

## **Warning: Legal and Ethical Disclaimer**

**WARNING: This project is intended solely for educational purposes and should only be executed in a controlled, sandboxed environment. Use of this software on any real-world systems is highly illegal and can result in severe criminal penalties, including imprisonment. The creator of this project is not responsible for any inappropriate use. YOU HAVE BEEN WARNED.**

This project includes a built-in kill switch to ensure it does not cause real harm. The intention of this file is **NOT TO HARM** but to understand the inner workings of common ransomware applications. This is a study and a proof of concept.

## **Project Overview**

### **About KRYPT0S**

KRYPT0S is a sophisticated Python ransomware simulation designed to demonstrate the complexities and operations of real-life ransomware. Its primary aim is educational, helping cybersecurity professionals and enthusiasts understand how ransomware works to better defend against such threats.

### **Key Features**

KRYPT0S employs various sophisticated techniques to ensure its effectiveness and stealth:

- **Complex Encryption Handling**: Utilizes AES encryption to lock files on Windows machines.
- **Persistence and Stealth**: Gains persistence by modifying system settings and running in the background, even after system reboots.
- **Ransomware Screen**: Displays a realistic-looking ransomware message similar to WannaCry. **All information, including Bitcoin addresses and buttons, is fake and generated for simulation purposes only.**
- **Stealth Tactics**: Disables Windows Defender, stops security services, and deletes shadow copies to prevent easy recovery.
- **Parallel Encryption**: Uses multi-threading to encrypt files across all drives efficiently.
- **Event Log Removal**: Attempts to clear Windows event logs to cover its tracks.
- **Vast Encryption**: Encrypts a wide range of file types across ALL drives using AES encryption, this also includes encyrption of '.exe' files in certain locations, maximising the damage.
- **Secure Keys**: The encryption key is generated in a manner that makes it difficult for potential forensics to uncover, including zeroing out data and special handling of the key in certain parts of memory.
- **Change System Wallpaper**: Changes system wallpaper to indicate an attack has occured, inducing fear into the victim. (Simulated)

## **Detailed Functionality**

## **No Decryption Function Present**

A key feature of KRYPT0S is the lack of a decryption algorithm, meaning encrypted files cannot be retrieved. This design mirrors real-world ransomware, emphasizing the severe consequences of such malware.

Once encrypted, file extensions change, making decryption and identification difficult. This becomes even more challenging if multiple machines are infected, resulting in a chaotic decryption process. Ransomware often falsely promises data recovery upon payment, as seen with WannaCry, which rarely allowed full file recovery after ransom payment.

This tactic manipulates victims into believing that paying will solve the problem, but it rarely does and encourages more attacks. The absence of a decryption function in KRYPT0S underscores the need for robust cybersecurity. Experts advise against paying the ransom, as it doesn’t guarantee data return and fuels cybercrime. Instead, focus on prevention, regular backups, and strong security protocols to mitigate ransomware risks.

### **Ransomware Screen**

The program includes a fake ransomware screen that mimics the appearance of the WannaCry ransomware, providing a realistic simulation environment:

- **Fake Bitcoin Address and Information**: All displayed information is fake and generated for simulation purposes. None of it is real.
- **Simulated Buttons and Functionality**: The screen is designed to look realistic, but all buttons and functions are simulated and have no real effect.
- **Preventing Closure**: The ransomware screen disables the close button (X) and removes the Alt+F4 bindings to prevent the tab from being closed. It also makes it difficult to terminate using traditional task manager methods.
- **Enhanced Persistence**: The screen continues to add persistence by checking if the registry key exists every few seconds, preventing its removal.

![image](https://github.com/user-attachments/assets/d3d7814d-7520-484a-b510-c3b9c5ad07c4)

## **Ethical and Safe Usage**

This project should be used only for educational purposes in a safe, controlled environment. It is equipped with a **kill switch** that stops the ransomware if a certain condition is met. This ensures that it does not cause any real harm during testing and educational use.

### **Running the Simulation**

To run KRYPT0S, follow these steps in a sandboxed environment:

1. **How to Run**: Convert both .py files to an .exe file (using the kryptos converter). Proceed to run "KRYPT0S.exe", the "Screen.exe" will run at the end.
   
_The converter used in this repository ensures you are running on a windows enviroment, running it in a UNIX enviroment will not work!_

Upon execution, KRYPT0S will identify all present drives and initiate encryption of all content within its specified extension range. This includes the encryption of .exe files in critical locations such as "/Downloads", "/OneDrive", and more. The destructive nature of KRYPT0S is severe, causing the system to halt due to the loss of sensitive and essential information. Such tactics are designed to induce a clear message of fear and destruction, highlighting the critical importance of protecting against these types of attacks.

**Remember: This program is for educational purposes only. !Do not use it on any real-world systems!**

### **Kryptos in Action**

_Aftermath of homescreen after attack_

![Aftermath-gif](https://github.com/user-attachments/assets/d99e527d-c4dc-4503-b03a-ea3ef7b69a76)

_Files encyrpted_

![image](https://github.com/user-attachments/assets/6d9cd5a8-93a7-4663-af5e-6981fc7fa9b9)

## **Conclusion**

KRYPT0S is a powerful and complex Python ransomware simulation designed to educate and inform about the workings of real ransomware. By understanding these mechanisms, cybersecurity professionals can better defend against such threats. Always use responsibly and within the bounds of the law.

---

**Disclaimer**: The author is not responsible for any misuse of this software. Use it only for educational purposes in controlled environments.
