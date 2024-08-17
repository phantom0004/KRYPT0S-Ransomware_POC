## Overview
![sniffer](https://github.com/user-attachments/assets/53ae63f4-f5ca-473c-b7ee-94a2b62a6e69)

**Ransomsniffer** is a tool designed to detect and analyze potentially malicious files, including ransomware. It provides two modes of operation:

1. **VirusTotal Scan (API Key Required)**: Submit a file or hash to VirusTotal for an in-depth analysis using multiple antivirus engines. This option offers comprehensive information about potential threats.

2. **Default Scan (YARA/Pefile)**: Perform a static scan using YARA rules and Pefile to identify common malicious patterns. This method can quickly flag suspicious files, including well-known ransomware like KRYPT0S.

## Features

- **Detect Malicious Files**: Identify and analyze files that may pose a security risk.
- **Ransomware Detection**: Capable of detecting ransomware files by recognizing known patterns.
- **VirusTotal Integration**: Optionally integrate with VirusTotal to leverage their extensive database for detailed threat reports.
- **Work in Progress**: This tool is currently under development. Future updates will improve its detection capabilities and add more features.

## How to Get Started

1. **VirusTotal API Key (Optional)**:
   - Sign up at VirusTotal: [VirusTotal Sign Up](https://www.virustotal.com/signup/)
   - After logging in, retrieve your API key from your profile under "API Key."
   - Paste the API key when prompted after selecting the VirusTotal scan option.

2. **Default Scan**:
   - No setup required. Just run the tool and choose the default scan option for a quick analysis.

## Important Notes

- **Not Ready for Use**: Ransomsniffer is currently in development and is not ready for production use. Testing is ongoing, and the tool should be used with caution.
- **Detection Limitations**: While Ransomsniffer can detect some types of ransomware and malicious files, it is not foolproof and should be part of a broader security strategy.

## Future Updates

This tool will receive continuous updates to enhance its capabilities and expand its detection range. Stay tuned for new features and improvements.
