# ScanSentinel v1.0.0

## Overview

**ScanSentinel** is a modern network discovery tool that combines traditional scanning techniques with **AI-powered reporting**. Unlike tools that only output raw scan results, ScanSentinel produces **structured reports**, highlights key findings, and guides the next steps in the network analysis workflow.

It is designed to be both:

* **Educational** — teaching users how network scanning works
* **Practical** — a tool that can be used for real discovery tasks

---

## How ScanSentinel Works

The tool operates in **two stages**:

### Stage 1 — Core Discovery

* Detects live hosts on a network
* Identifies open and closed ports
* Collects operating system and architecture information
* Detects services and running processes
* Attempts to detect firewalls or other security devices
* Saves raw results for further analysis

### Stage 2 — AI Reporting

* Interprets scan results into clear, understandable language
* Structures findings into a `report.md` file
* Highlights key discoveries across hosts, services, and systems
* Provides actionable insights for next steps (vulnerability detection and exploitation are planned for future stages)

This approach makes network discovery more **efficient, repeatable, and educational**.

---

## Features

* **Flexible Target Input** — supports hostnames, IP ranges, or entire networks
* **AI-Powered Reporting** — transforms raw scan results into structured, actionable reports
* **Modular Design** — designed to expand into future stages like Vulnerability Analysis and Exploitation

---

## System Requirements

Since **ScanSentinel integrates AI inference** using **Mistral 7B Instruct**, system requirements are higher than standard scanning tools.

### Minimum

* **OS:** Linux (tested on Ubuntu/Debian)
* **CPU:** Quad-core (x86\_64)
* **RAM:** 8 GB — sufficient for **quantized AI model** inference
* **Disk Space:** \~10 GB (includes scanning tools, AI runtime, and model \~4–5 GB)
* **Notes:** Inference may be slower without GPU acceleration

### Recommended

* **CPU:** 6+ cores for faster inference and multitasking
* **RAM:** 16 GB or more
* **GPU (optional):** CUDA-compatible GPU to speed up AI inference
* **Disk Space:** 15 GB+ for multiple models and caching

**Additional Notes**

* Ollama handles **memory-efficient quantized AI models**, making local inference feasible
* Without GPU, AI reporting will be slower but fully functional
* Tested on Linux; other OS may require adjustments

---

## Installation

### Linux

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd ScanSentinel
   ```

2. Run the setup script:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

This script will:

* Install necessary scanning tools
* Install **AI runtime (Ollama)**
* Download the default AI model (\~5 GB)
* Prepare the environment to run `ScanSentinel.py`

---

## Usage

### Run a Scan

```bash
python3 ScanSentinel.py <target>
```

Examples:

```bash
python3 ScanSentinel.py 192.168.1.10
python3 ScanSentinel.py 192.168.1.0/24
```

If no target is specified, ScanSentinel will prompt interactively.

After execution, ScanSentinel will:

* Run discovery scans and save raw results
* Generate structured AI-driven `report.md`
* Print a summary to the terminal

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

## Roadmap — v1.1.0 (Discovery Focus)

Target release: **September 29**

The **Discovery stage** is the primary focus:

* Identify live hosts
* Map open and closed ports
* Collect OS and system architecture info
* Detect running services and processes
* Identify security devices (firewalls, etc.)
* Provide initial insights into potential vulnerabilities

All findings will be **structured in reports**, forming the foundation for future stages.

## Contributing

Contributions are welcome!

* Open issues for bugs or ideas
* Submit pull requests to improve functionality or documentation
