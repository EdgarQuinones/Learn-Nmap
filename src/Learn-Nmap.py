import os
import subprocess
import xml.etree.ElementTree as ET
import sys
import time  # <-- Added for timing

# ANSI color codes
RED = "\033[91m"      # Closed / filtered / errors
GREEN = "\033[92m"    # Open ports
YELLOW = "\033[93m"   # Host headers / summary labels
CYAN = "\033[96m"     # Intro / summary headers
RESET = "\033[0m"

# Subprocess variables
xml_file = "output.xml"
ollama_model = "llama3.1:8b"
ollama_prompt = """
---

**AI Prompt: Dynamic Nmap Analyzer with Example Report**

> You are an expert in network scanning and penetration testing. Your task is to analyze an Nmap scan report and generate **service-specific Nmap recommendations with increasing intrusion levels** for every detected service.
>
> **Instructions:**
>
> 1. Analyze the Nmap report and identify **all live hosts, open ports, and running services**.
> 2. For **each service**, generate **four levels of Nmap commands**:
>
>    * **Level 1 (Safe Scan):** Minimal intrusion, basic confirmation of the service.
>    * **Level 2 (Moderate Scan):** Version/service detection and OS fingerprinting if safe.
>    * **Level 3 (Aggressive Scan):** Include relevant NSE scripts to check common vulnerabilities.
>    * **Level 4 (Exhaustive/Intrusive Scan):** All recommended scripts/options; high intrusion (ensure legal permission).
> 3. Automatically choose **NSE scripts appropriate for the service** (e.g., `http-enum` for HTTP, `ssh-hostkey` for SSH, `ftp-anon` for FTP, `smb-enum*` for SMB, etc.).
> 4. Provide **full example Nmap commands** for each level per service.
> 5. Include practical tips for using Nmap efficiently in subsequent scans.
> 6. Highlight other insights, follow-up actions, or next steps useful for penetration testing or network analysis.

> **Example Nmap Report (Fake):**

```
Host: 192.168.1.10
Open Ports:
- 22/tcp (SSH)
- 80/tcp (HTTP)
- 443/tcp (HTTPS)
- 139/tcp (SMB)
- 3306/tcp (MySQL)
```

> **Expected Output Structure:**

```
Summary of Findings:
- Host(s) and IPs:
- Open ports and associated services:
- Notable results (vulnerabilities, unusual configurations, etc.):

Service-Specific Recommendations:

Service: [detected service] on port [port number]
- Level 1 (Safe Scan): [full Nmap command] — [brief description]
- Level 2 (Moderate Scan): [full Nmap command] — [brief description]
- Level 3 (Aggressive Scan): [full Nmap command with relevant NSE scripts] — [brief description]
- Level 4 (Exhaustive/Intrusive Scan): [full Nmap command with all recommended scripts/options] — [brief description]

Service: [next detected service] on port [port number]
- Level 1:
- Level 2:
- Level 3:
- Level 4:

Tips for Next Scans:
- Tip 1
- Tip 2

Additional Recommendations:
- Any other useful insights or follow-up actions
```

> **Notes for AI:**
>
> * For unknown or uncommon services, suggest generic NSE scripts that provide safe service enumeration.
> * Always ensure Level 1 scans are low-intrusion and Level 4 scans are exhaustive/highly intrusive.
> * Combine ports of the same service into one command where appropriate to improve efficiency.
> * Output should be ready to use as a reference sheet of commands per service.

---

example format you should follow : 
```
Host: 192.168.1.10
Open Ports:
- 22/tcp (SSH)
- 80/tcp (HTTP)
- 443/tcp (HTTPS)
- 139/tcp (SMB)
- 3306/tcp (MySQL)
```

**AI-Generated Output:**

```
Summary of Findings:
- Host: 192.168.1.10
- Open ports and associated services:
  - 22/tcp: SSH
  - 80/tcp: HTTP
  - 443/tcp: HTTPS
  - 139/tcp: SMB
  - 3306/tcp: MySQL
- Notable results: Services are standard; no unusual configurations detected.

Service-Specific Recommendations:

Service: SSH on port 22
- Level 1 (Safe Scan): nmap -p 22 192.168.1.10 — Basic port check
- Level 2 (Moderate Scan): nmap -sV -p 22 192.168.1.10 — Version/service detection
- Level 3 (Aggressive Scan): nmap -sV --script=ssh-hostkey,ssh-auth-methods -p 22 192.168.1.10 — Aggressive scan with SSH enumeration scripts
- Level 4 (Exhaustive/Intrusive Scan): nmap -sV --script=ssh-hostkey,ssh-auth-methods,ssh-brute -p 22 192.168.1.10 — Exhaustive scan including brute-force testing (ensure legal permission)

Service: HTTP on port 80
- Level 1: nmap -p 80 192.168.1.10 — Basic port check
- Level 2: nmap -sV -p 80 192.168.1.10 — Version/service detection
- Level 3: nmap -sV --script=http-enum,http-title,http-methods -p 80 192.168.1.10 — Aggressive scan with common HTTP scripts
- Level 4: nmap -sV --script=http-enum,http-vuln*,http-slowloris* -p 80 192.168.1.10 — Exhaustive HTTP scan including vulnerability scripts

Service: HTTPS on port 443
- Level 1: nmap -p 443 192.168.1.10 — Basic port check
- Level 2: nmap -sV -p 443 192.168.1.10 — Version/service detection
- Level 3: nmap -sV --script=http-enum,http-title,http-methods,ssl-cert -p 443 192.168.1.10 — Aggressive scan including SSL certificate info
- Level 4: nmap -sV --script=http-enum,http-vuln*,http-slowloris*,ssl-* -p 443 192.168.1.10 — Exhaustive HTTPS scan

Service: SMB on port 139
- Level 1: nmap -p 139 192.168.1.10 — Basic port check
- Level 2: nmap -sV -p 139 192.168.1.10 — Version/service detection
- Level 3: nmap -sV --script=smb-enum-shares,smb-enum-users -p 139 192.168.1.10 — Aggressive SMB enumeration
- Level 4: nmap -sV --script=smb-enum*,smb-vuln* -p 139 192.168.1.10 — Exhaustive SMB scan including vulnerability checks

Service: MySQL on port 3306
- Level 1: nmap -p 3306 192.168.1.10 — Basic port check
- Level 2: nmap -sV -p 3306 192.168.1.10 — Version/service detection
- Level 3: nmap -sV --script=mysql-info,mysql-empty-password -p 3306 192.168.1.10 — Aggressive MySQL scripts
- Level 4: nmap -sV --script=mysql-* -p 3306 192.168.1.10 — Exhaustive MySQL scan

Tips for Next Scans:
- Use `-oA` to save output in all formats for documentation.  
- Adjust timing (`-T3` to `-T5`) depending on network stability.  
- For multi-host scans, use ranges or CIDR notation (e.g., `192.168.1.0/24`).

Additional Recommendations:
- Cross-check discovered services with known CVEs for vulnerabilities.  
- Consider follow-up enumeration with specialized tools for SSH, SMB, or MySQL if Level 4 scans reveal potential issues.  
- Document findings in a structured report for the next phase of penetration testing.
```

THE FOLLOWING REPORT IS THE ONE YOU SHOULD ANALYZE: 
"""

# Fancy boxed intro
intro = (
    "="*60 + "\n" +
    f"{CYAN}                  --- Learn-Nmap ---{RESET}\n" +
    f"{CYAN}       Automates Nmap scans and generates a report.{RESET}\n" +
    "="*60 + "\n"
)

# Determine target
if len(sys.argv) == 2:
    print(intro)
    target = sys.argv[1]
else:
    print("="*60)
    print(f"{RED}ERROR: Invalid arguments!{RESET}")
    print("Usage:")
    print("  Learn-Nmap.py <Host or Network>")
    print("="*60)
    sys.exit(1)

print("\nScanning...\n")

# Run Nmap in background
nmap_scan = subprocess.run(
    ["nmap", target, "-oX", xml_file],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

nmap_output = nmap_scan.stdout
print("Generating report...\n")

# Track Olama report generation time
start_time = time.time()

ollama_data = subprocess.run(
    [
        "ollama", "run", ollama_model,
        f"{ollama_prompt} {nmap_output}"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

end_time = time.time()
report_time = end_time - start_time

report = ollama_data.stdout

# Save the Olama report to a file
report_file = "report.md"
with open(report_file, "w") as f:
    f.write(report + "\n")

# Parse XML output
scan_root = ET.parse(xml_file).getroot()
os.system(f"rm {xml_file}")

summary = scan_root.find("runstats/finished").attrib.get("summary", "")

hosts_with_open_ports = []
hosts_without_open_ports = []

# Iterate over hosts
for host in scan_root.findall("host"):
    ip_addr = host.find("address").attrib["addr"]
    ports_elem = host.find("ports")
    port_list = ports_elem.findall("port") if ports_elem is not None else []

    if port_list:
        hosts_with_open_ports.append(ip_addr)
        print(f"{YELLOW}Services running for host {ip_addr}:{RESET}")
        for port in port_list:
            portid = port.attrib["portid"]
            protocol = port.attrib["protocol"]
            state = port.find("state").attrib.get("state", "unknown")
            service_elem = port.find("service")
            service_name = service_elem.attrib["name"] if service_elem is not None else "unknown"

            # Color based on state
            color = GREEN if state == "open" else RED
            print(f"  {color}- {service_name} on {protocol}/{portid} ({state}){RESET}")
    else:
        hosts_without_open_ports.append(ip_addr)
        print(f"{YELLOW}Host {ip_addr} has no open ports.{RESET}")

    print()  # blank line for readability

# Summary box
summary_box = (
    "="*60 + "\n" +
    f"{CYAN}                  --- Scan Summary ---{RESET}\n\n" +
    f"{YELLOW}Hosts with open ports:{RESET} {len(hosts_with_open_ports)}\n" +
    (f"{', '.join(hosts_with_open_ports)}\n" if hosts_with_open_ports else "None\n") +
    f"{YELLOW}Hosts with no open ports:{RESET} {len(hosts_without_open_ports)}\n" +
    (f"{', '.join(hosts_without_open_ports)}\n" if hosts_without_open_ports else "None\n") +
    f"{YELLOW}Nmap run summary:{RESET} {summary}\n" +
    "="*60
)
print(summary_box)

# Notify user about Olama report and time, combined neatly
print(
    f"{CYAN}A report has been written to file: {report_file}\n"
    f"Report generation time: {report_time:.2f} seconds{RESET}"
)

