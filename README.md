# Learn-Nmap

**Learn-Nmap** is a Python tool that integrates **Nmap** with **AI-powered analysis**, making scans more efficient and generating actionable reports with recommended next steps.

---

## Features

* **Flexible Target Input**
  Accepts a host, IP range, or network.

* **Automated Nmap Scans**
  Detects live hosts, open ports, and running services.

* **AI-Powered Analysis**
  Uses Ollama with the `llama3.1:8b` model to interpret scan results.

* **Progressive Recommendations**
  Suggests Nmap commands at four levels of intrusion (from safe to exhaustive).

* **Actionable Reporting**
  Saves results to `report.md`, including summaries, recommended scripts, and follow-up tips.

---

## Installation

### Linux

1. Clone the repository and enter the directory:

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

* **Batch Script**

  1. Save the script as `setup.bat`.
  2. Right-click and select *Run as Administrator*.

* **PowerShell**

  1. Save the script as `setup.ps1`.
  2. Open PowerShell as Administrator.
  3. Run:

     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; .\setup.ps1
     ```

These scripts will:

* Install **Nmap**
* Install **Ollama**
* Start the Ollama service
* Download the **llama3.1:8b** model (\~4.7 GB)
* Prepare the environment to run `Learn-Nmap.py`

---

## Usage

### Run a Scan

```bash
python3 Learn-Nmap.py <target>
```

Examples:

```bash
python3 Learn-Nmap.py 192.168.1.10
python3 Learn-Nmap.py 192.168.1.0/24
```

After execution, the script will:

* Run **Nmap** and save raw results.
* Use **AI** to generate a structured report (`report.md`).
* Print a color-coded summary to the terminal.

---

## Example Output

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

## Project Philosophy

**Learn-Nmap** bridges the gap between manual scanning and automated analysis.
Rather than only running Nmap, it provides **AI-driven recommendations** tailored to each detected service.

The objective is to minimize repetitive tasks and enable penetration testers to focus on interpreting results and taking action.

---

## Contributing

Contributions, ideas, and bug reports are welcome.
Please open an issue or submit a pull request to help improve **Learn-Nmap**.
