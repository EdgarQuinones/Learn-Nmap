# Learn Nmap

A Python tool that leverages AI to make **Nmap scans smarter and more efficient**, generating detailed, actionable reports that explain findings and suggest next steps.

---

## 🚀 Features

* **Target Input:** Enter a host, IP range, or network.
* **Automated Nmap Scan:** Detects open ports and running services.
* **AI-Powered Analysis:** Uses Ollama + `llama3.1:8b` to analyze results.
* **Progressive Recommendations:** For each service, the AI suggests Nmap commands at 4 intrusion levels (safe → exhaustive).
* **Actionable Reporting:** Saves results to `report.md` with summary, recommended scripts, and follow-up tips.

---

## 🛠️ Installation

### Linux

1. Clone the repo and move into the folder:

   ```bash
   git clone <repo-url>
   cd learn-nmap
   ```
2. Run the setup script:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

### Windows

* **Batch Script:**

  1. Save as `setup.bat`
  2. Right-click → *Run as Administrator*

* **PowerShell:**

  1. Save as `setup.ps1`
  2. Open PowerShell as Administrator
  3. Run:

     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; .\setup.ps1
     ```

✅ These scripts will:

* Install **Nmap**
* Install **Ollama**
* Start the Ollama service
* Download the **llama3.1:8b** model (\~4.7GB)
* Prepare everything to run `Learn-Nmap.py`

---

## ▶️ Usage

### Run a Scan

```bash
python3 Learn-Nmap.py <target>
```

Examples:

```bash
python3 Learn-Nmap.py 192.168.1.10
python3 Learn-Nmap.py 192.168.1.0/24
```

* If no argument is given, you will be prompted to enter a target.
* After scanning, the script will:

  * Run **Nmap** and save raw results.
  * Use **AI** to generate a structured report (`report.md`).
  * Print a color-coded summary in the terminal.

---

## 📄 Output Example

```
Summary of Findings:
- Host: 192.168.1.10
- Open ports and associated services:
  - 22/tcp: SSH
  - 80/tcp: HTTP
  - 443/tcp: HTTPS
  - 139/tcp: SMB
  - 3306/tcp: MySQL

Service-Specific Recommendations:
Service: SSH on port 22
- Level 1: nmap -p 22 192.168.1.10 — Basic port check
- Level 2: nmap -sV -p 22 192.168.1.10 — Version detection
- Level 3: nmap -sV --script=ssh-hostkey,ssh-auth-methods -p 22 192.168.1.10
- Level 4: nmap -sV --script=ssh-brute,ssh-hostkey,ssh-auth-methods -p 22 192.168.1.10

Tips for Next Scans:
- Use `-oA` to save output in all formats.
- Increase `-T` speed carefully based on stability.
```

---

## 💡 Project Philosophy

This project was built to bridge **manual scanning** and **automated analysis**.
Instead of just running Nmap, security teams get **AI-powered recommendations** tailored to each service.

The goal is to reduce repetitive tasks and help penetration testers focus on what matters: **interpreting results and taking action**.

---

## 🤝 Contributing

Contributions, ideas, and bug reports are welcome.
Please open an issue or submit a PR to help improve **Learn-Nmap**.
