# Learn Nmap

A script that leverages AI to make Nmap more efficient, generating detailed reports that explain its findings.

---

## 🚀 Main Features

- **User Input:** Specify host/network and intrusion level (1-4)
- **Automated Scanning:** Detects open ports and services
- **Targeted Scripts:** Runs service-specific Nmap scripts
- **Reporting:** Produces actionable reports with next steps

---

## 🛠️ Usage Instructions

### Linux

1. Save the script as `setup.sh`
2. Make it executable:
    ```bash
    chmod +x setup.sh
    ```
3. Run the script:
    ```bash
    ./setup.sh
    ```

### Windows

- **Batch Script:**
  1. Save as `setup.bat`
  2. Right-click and select "Run as Administrator"

- **PowerShell:**
  1. Save as `setup.ps1`
  2. Open PowerShell as Administrator
  3. Run:
      ```powershell
      Set-ExecutionPolicy Bypass -Scope Process -Force; .\setup.ps1
      ```

**These scripts will:**
- Install Nmap
- Install Ollama
- Start the Ollama service
- Download the `llama3.1:8b` model (~4.7GB)
- Set up everything needed to run `Learn-Nmap.py`

---

## 💡 Project Philosophy

I created this project out of a passion for cybersecurity and programming. While live penetration testing can be stressful, I thrive in methodical planning and tool development. My aim is to empower security teams with flexible automation that enhances their capabilities.

I welcome feedback from security professionals to improve these scripts. Your insights help make this tool more useful for real-world security work. Thank you for exploring this project—I hope it adds value to your workflow!

---

## 🤝 Contributing

Feedback, bug reports, and suggestions are always appreciated. Community input and real-world testing make this project stronger!

