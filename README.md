# Learn-Nmap v1.0.0

## Overview

**Nmap** is one of the most widely used penetration testing tools, supporting:

* Host discovery
* Port scanning
* Service detection
* Vulnerability identification

It has been a cornerstone of reconnaissance work for decades.

**Learn-Nmap** builds on this foundation by combining **Nmap scanning** with **AI-powered reporting**. Instead of just running raw scans, it automates the process and generates **structured, actionable reports** with next-step recommendations.

---

## How Learn-Nmap Works

The tool operates in **two stages**:

### Stage 1 — Core Scanning

* Identifies live hosts
* Detects open ports and running services
* Collects OS details
* Saves raw scan results

### Stage 2 — AI Interpretation

* Uses **Ollama** with the `llama3.1:8b` model
* Summarizes findings in plain English
* Generates a structured `report.md`
* Provides progressive Nmap recommendations (Level 1 → Level 4)

This approach bridges the gap between manual scanning and automated analysis, making results easier to understand and apply.

---

## Features

* **Flexible Target Input** — hostnames, IP ranges, or networks
* **AI-Powered Analysis** — contextual recommendations for each service
* **Actionable Reporting** — saves results in Markdown format
* **Progressive Nmap Commands** — tailored for beginner to advanced testers

---

## System Requirements

Since Learn-Nmap integrates **AI inference**, system requirements vary depending on usage.

### Minimum (to run Nmap + AI locally)

* **OS:** Linux (tested on Ubuntu/Debian)
* **CPU:** Quad-core (x86\_64)
* **RAM:** 8 GB
* **Disk Space:** \~10 GB (Nmap, Ollama, and llama3.1:8b model \~4.7 GB)

### Recommended (for smooth AI performance)

* **CPU:** 6+ cores
* **RAM:** 16 GB or more
* **GPU (optional):** A CUDA-compatible GPU improves response times
* **Disk Space:** 15 GB+

💡 If your machine struggles with local inference, consider using a **smaller model** in Ollama or offloading AI analysis to a remote/paid API.

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
* Install **Ollama**
* Start the Ollama service
* Download the `llama3.1:8b` model (\~4.7 GB)
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
* Print a color-coded summary to the terminal

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

## Roadmap — v1.1.0 (DISCOVERY Update)

Target release: **September 29** (before CPTC)

Goals for the **Discovery module (`Learn-Discover.py`)**:

* Automate host/service/port/OS scanning
* Integrate additional Nmap discovery scripts
* Merge results into structured reports
* Add AI-powered summaries for:

  * Domain names
  * IPs
  * Services & versions
  * OS details
* Provide **pre-scan guidance** (planning & OSINT reminders)
* Focus strictly on **information gathering** (no exploitation)

---

## Long-Term Stages

The project roadmap follows a phased penetration testing workflow:

1. **Discovery**
2. **Vulnerabilities**
3. **Exploitation**

Each stage builds on the previous one, with AI support for both automation and interpretation.

---

## Contributing

Contributions are welcome!

* Open an issue for bugs/ideas
* Submit a pull request to improve functionality or documentation
