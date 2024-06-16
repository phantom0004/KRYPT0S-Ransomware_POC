# _KRYPT0S : Encrypt, Conceal, Control

## **Warning: Legal and Ethical Disclaimer**

**WARNING: This project is intended solely for educational purposes and should only be executed in a controlled, sandboxed environment. Use of this software on any real-world systems is highly illegal and can result in severe criminal penalties, including imprisonment. The creator of this project is not responsible for any inappropriate use. YOU HAVE BEEN WARNED.**

This project includes a built-in kill switch to ensure it does not cause real harm. The intention of this file is **NOT TO HARM** but to understand the inner workings of common ransomware applications. This is a study and a proof of concept.

## **Project Overview**

### **About _KRYPT0S**

_KRYPT0S_ is a sophisticated Python ransomware simulation designed to demonstrate the complexities and operations of real-life ransomware. Its primary aim is educational, helping cybersecurity professionals and enthusiasts understand how ransomware works to better defend against such threats.

### **Key Features**

- **Complex Encryption Handling**: Utilizes AES encryption to lock files on Windows machines.
- **Persistence and Stealth**: Gains persistence by modifying system settings and running in the background, even after system reboots.
- **Ransomware Screen**: Displays a realistic-looking ransomware message similar to WannaCry. **All information, including Bitcoin addresses and buttons, is fake and generated for simulation purposes only.**
- **Stealth Tactics**: Disables Windows Defender, stops security services, and deletes shadow copies to prevent easy recovery.
- **Parallel Encryption**: Uses multi-threading to encrypt files across all drives efficiently.

## **Detailed Functionality**

### **Sophistication and Stealth**

_KRYPT0S_ employs various sophisticated techniques to ensure its effectiveness and stealth:

- **Startup Commands**: Disables security services and shadow copies, modifies boot policies to prevent recovery, and stops various antivirus processes.
- **Encryption**: Encrypts a wide range of file types across all detected drives using AES encryption. The encryption key is generated in a manner that makes it difficult for potential forensics to uncover, including zeroing out data and special handling of the key in certain parts of memory.
- **Event Log Removal**: Attempts to clear Windows event logs to cover its tracks.
- **Persistence**: Modifies the Windows registry to ensure it runs at startup, maintaining persistence across reboots.

## **No Decryption Function Present**

One critical aspect of _KRYPT0S_ is the absence of a decryption algorithm. This means that once your files have been encrypted, there is no built-in method to retrieve them. Similar to many real-world ransomware attacks, this design underscores the severe and often irreversible consequences of such malware.

Once encryption has occurred, the file extensions are altered, making it incredibly difficult to decrypt and identify the original files. This complexity is compounded when multiple machines are infected, leading to a chaotic and nearly impossible decryption process. Real-world ransomware often promises victims that they will regain access to their data upon payment. However, this promise is frequently broken. For instance, the WannaCry ransomware allowed partial decryption, but the likelihood of fully recovering all files after paying the ransom was extremely low.

This deceptive tactic is a psychological manipulation, creating a false sense of security that paying the ransom will solve the problem. In reality, paying the ransom rarely guarantees file recovery and only fuels the ransomware economy, encouraging further attacks.

The lack of a decryption function in _KRYPT0S_ serves as a stark reminder of the importance of understanding and preparing for ransomware threats. It highlights the critical need for robust cybersecurity measures and reinforces the advice of cybersecurity experts: **Never pay the ransom**. Paying not only fails to guarantee the return of your data but also perpetuates the cycle of cybercrime. It is essential to focus on prevention, regular backups, and comprehensive security protocols to mitigate the risk and impact of ransomware attacks.

### **Ransomware Screen**

The program includes a fake ransomware screen that mimics the appearance of the WannaCry ransomware, providing a realistic simulation environment:

- **Fake Bitcoin Address and Information**: All displayed information is fake and generated for simulation purposes. None of it is real.
- **Simulated Buttons and Functionality**: The screen is designed to look realistic, but all buttons and functions are simulated and have no real effect.
- **Preventing Closure**: The ransomware screen disables the close button (X) and removes the Alt+F4 bindings to prevent the tab from being closed. It also makes it difficult to terminate using traditional task manager methods.
- **Enhanced Persistence**: The screen continues to add persistence by checking if the registry key exists every few seconds, preventing its removal.

![image](https://github.com/phantom0004/_KRYPT0S_RANSOMWARE/assets/42916447/4c7d4641-8d20-45f3-8515-6efc7212d485)

## **Ethical and Safe Usage**

This project should be used only for educational purposes in a safe, controlled environment. It is equipped with a kill switch that stops the ransomware if a certain condition is met. This ensures that it does not cause any real harm during testing and educational use.

### **Running the Simulation**

To run _KRYPT0S_, follow these steps in a sandboxed environment:

1. **Initial Check**: The program attempts to connect to a specific URL. If the connection is successful, it will terminate itself.
2. **System Commands**: Disables security measures and prepares the system for encryption.
3. **Encryption Process**: Encrypts files on all detected drives using AES encryption.
4. **Display Ransomware Screen**: Launches the fake ransomware screen to complete the simulation.

**Remember: This program is for educational purposes only. Do not use it on any real-world systems.**

## **Conclusion**

_KRYPT0S_ is a powerful and complex Python ransomware simulation designed to educate and inform about the workings of real ransomware. By understanding these mechanisms, cybersecurity professionals can better defend against such threats. Always use responsibly and within the bounds of the law.

---

Feel free to contribute to this project by submitting issues or pull requests. For any questions or concerns, please contact the project maintainer.

---

**Disclaimer**: The author is not responsible for any misuse of this software. Use it only for educational purposes in controlled environments.
