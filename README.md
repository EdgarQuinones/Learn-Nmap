# Learn-Nmap v1.0.0

## Overview

**Nmap** is one of the most widely used penetration testing tools, supporting:

* Host discovery
* Port scanning
* Service detection
* Vulnerability identification

It remains a cornerstone of reconnaissance work for ethical hackers and penetration testers.

**Learn-Nmap** enhances this workflow by combining **Nmap scanning** with **AI-powered reporting**. Instead of leaving results in raw scan outputs, the tool generates **structured reports** that summarize findings, highlight key details, and guide the next steps.

---

## How Learn-Nmap Works

The tool operates in **two stages**:

### Stage 1 — Core Scanning

* Detects live hosts
* Identifies open and closed ports
* Collects operating system information
* Identifies services and running processes
* Detects system architecture details
* Attempts to detect firewalls or other security devices
* Saves raw results for later analysis

### Stage 2 — AI Reporting

* Interprets scan results into plain English
* Structures findings into a `report.md` file
* Highlights key discoveries across hosts, services, and systems
* Includes potential vulnerabilities (when identifiable), though this is not the main focus until the **Vulnerability stage**

This approach makes discovery more **efficient, repeatable, and educational**.

---

## Features

* **Flexible Target Input** — accepts hostnames, IP ranges, or entire networks
* **AI-Driven Reporting** — scan results transformed into structured, actionable reports
* **Cross-Stage Alignment** — designed to evolve into future modules (Vulnerabilities, Exploitation)

---

## System Requirements

Since **Learn-Nmap integrates AI inference** using **Mistral 7B Instruct**, system requirements are higher than standard Nmap usage.

### Minimum

* **OS:** Linux (tested on Ubuntu/Debian)
* **CPU:** Quad-core (x86\_64)
* **RAM:** 8 GB — sufficient only for **quantized model** inference
* **Disk Space:** \~10 GB (includes Nmap, AI runtime, and quantized model \~4–5 GB)
* **Notes:** Inference may be slow without GPU acceleration

### Recommended

* **CPU:** 6+ cores (faster inference and multitasking)
* **RAM:** 16 GB or more — ensures full quantized model loads comfortably alongside Nmap
* **GPU (optional):** CUDA-compatible GPU improves AI inference speed
* **Disk Space:** 15 GB+ — allows multiple models and caching

### Additional Notes

* **Quantization:** Ollama automatically handles memory-efficient model formats, making it feasible to run Mistral 7B Instruct on 16 GB RAM
* **Performance:** Without GPU, inference will be slower, but fully functional
* **Compatibility:** Tested on Linux; other OS may require adjustments

If your system struggles with local inference, consider using a smaller AI model or offloading analysis to a remote/paid service in future versions.

---

## Installation

### Linux

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd learn-nmap
   ```

2. Run the setup script:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

This script will:

* Install **Nmap**
* Install **AI runtime (Ollama)**
* Start the required service
* Download the default AI model (\~5 GB)
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

If no target is specified, the tool will prompt interactively.

After execution, Learn-Nmap will:

* Run **Nmap** and save raw results
* Use **AI** to create `report.md`
* Print a structured summary to the terminal

---

## Example Output

```
Summary of Findings:
- Host: 192.168.1.10
- Open ports and services:
  - 22/tcp: SSH
  - 80/tcp: HTTP
  - 443/tcp: HTTPS
  - 139/tcp: SMB
  - 3306/tcp: MySQL

System Details:
- Operating System: Linux (probable)
- Architecture: x86_64
- Firewall Detected: No
- Running Processes: sshd, apache2, mysqld
```

---

## Roadmap — v1.1.0 (DISCOVERY Update)

Target release: **September 29** (before CPTC)

The **Discovery stage** is the primary focus right now.
According to ethical hacking methodology, the objectives of network scanning are:

* Identify live hosts on a network
* Identify open & closed ports
* Identify operating system information
* Identify services running on a network
* Identify running processes on a network
* Identify the presence of security devices (e.g., firewalls)
* Identify system architecture
* Identify vulnerabilities (if possible, though not the priority yet)

These results will be **organized into reports**, forming the foundation for the next stages.

---

## Long-Term Stages

The project roadmap follows a phased penetration testing workflow:

1. **Discovery** (current focus)
2. **Vulnerabilities** (deeper vulnerability detection and analysis)
3. **Exploitation** (controlled testing of discovered weaknesses)

Each stage builds on the previous one, ensuring structure and clarity.

---

## Contributing

Contributions are welcome!

* Open an issue for bugs/ideas
* Submit a pull request to improve functionality or documentation
