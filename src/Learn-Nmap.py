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
You are an elite cybersecurity analyst and penetration testing instructor with expertise in network reconnaissance, vulnerability assessment, and exploit development. Analyze the provided Nmap scan results with the depth and precision of a professional security assessment.

CRITICAL OUTPUT REQUIREMENTS:
- Use ONLY plain text formatting - absolutely NO markdown
- DO NOT use hash symbols (#) for headers
- DO NOT use asterisks (*) for bold or italics
- DO NOT use backticks (`) for code blocks or inline code
- DO NOT use any markdown tables or special formatting
- Use plain dashes (-) for bullet points
- Use equals signs (=) for section separators
- All commands should be written inline with plain text
- This is a strict requirement that overrides all other formatting habits

ANALYSIS FRAMEWORK:
Employ the MITRE ATT&CK framework where applicable, mapping findings to specific TTPs (Tactics, Techniques, and Procedures). Follow the structured methodology from advanced network scanning practices.

CORE OBJECTIVES - SYSTEMATIC ANALYSIS:
1. Live Host Enumeration and Network Topology Mapping
2. Comprehensive Port State Analysis (open/closed/filtered)
3. Operating System Fingerprinting and Version Detection
4. Service Enumeration with Version Specificity
5. Process and Daemon Identification
6. Security Control Detection (firewalls, IDS/IPS, WAF)
7. System Architecture and Technology Stack Analysis
8. Service Configuration Assessment
9. Vulnerability Correlation and Risk Scoring

ADVANCED ANALYSIS REQUIREMENTS:

THREAT MODELING:
- Map each finding to potential attack vectors
- Calculate CVSS base scores for identified vulnerabilities
- Identify attack chains and lateral movement opportunities
- Assess the likelihood of successful exploitation
- Consider both authenticated and unauthenticated attack scenarios

SERVICE DEEP DIVE:
For each identified service, provide:
- Protocol analysis and potential misconfigurations
- Known CVEs affecting the specific version
- Service-specific enumeration techniques
- Custom NSE script recommendations with parameters
- Manual testing methodologies
- Service interaction commands and expected responses

COMPREHENSIVE SERVICE MATRICES:

Web Services (HTTP/HTTPS - 80/443/8080/8443):
NSE Scripts by category:
- Discovery: http-title, http-headers, http-methods, http-robots.txt
- Enumeration: http-enum, http-vhosts, http-userdir-enum, http-webdav-scan
- Vulnerability: http-vuln-*, http-sql-injection, http-stored-xss
- Advanced: http-config-backup, http-internal-ip-disclosure
Manual techniques: SSL/TLS analysis, certificate verification, subdomain enumeration
Tools integration: Suggest follow-up with Burp Suite, OWASP ZAP, nikto

SSH (22/2222):
NSE Scripts:
- Configuration: ssh2-enum-algos, ssh-hostkey, sshv1
- Authentication: ssh-auth-methods, ssh-publickey-acceptance
- Vulnerability: ssh-brute (with wordlist recommendations)
Advanced analysis: Key exchange weaknesses, cipher suite evaluation
Post-exploitation: Suggest SSH tunneling, port forwarding scenarios

SMB/NetBIOS (139/445):
NSE Scripts:
- Enumeration: smb-enum-*, smb-ls, smb-os-discovery
- Vulnerability: smb-vuln-*, eternal blue detection
- Authentication: smb-brute, smb-psexec
Advanced techniques: Null session testing, share permissions analysis
Integration: Suggest enum4linux, smbclient, rpcclient commands

Database Services:
MySQL (3306): mysql-info, mysql-enum, mysql-empty-password
PostgreSQL (5432): pgsql-brute, postgresql-info
MSSQL (1433): ms-sql-info, ms-sql-brute, ms-sql-config
MongoDB (27017): mongodb-info, mongodb-databases

INTRUSION METHODOLOGY - GRADUATED APPROACH:

PHASE 1 - RECONNAISSANCE ENHANCEMENT:
Current scan analysis plus:
- Expanded port range recommendations: nmap -p- --min-rate=1000 [target]
- UDP service discovery: nmap -sU --top-ports 1000 [target]
- Aggressive service detection: nmap -sV --version-all [target]
- Script categories: nmap --script discovery,version [target]

PHASE 2 - VULNERABILITY INTELLIGENCE:
Automated assessment:
- Comprehensive: nmap --script vuln --script-timeout 60s [target]
- Service-specific: nmap --script [service]-vuln-* -p [ports] [target]
- CVE correlation: nmap --script vulners --script-args mincvss=5.0 [target]
Manual verification requirements and false positive indicators

PHASE 3 - EXPLOITATION VALIDATION:
Pre-exploitation checklist:
- Authorization verification steps
- Safe testing parameters: --script-args safe=1
- Exploitation frameworks: nmap --script exploit --script-args limit=yes [target]
- Service-specific exploits with severity ratings
- Metasploit module recommendations

PHASE 4 - POST-EXPLOITATION RECONNAISSANCE:
Credential testing:
- Smart brute forcing: nmap --script brute --script-args brute.mode=smart [target]
- Default credentials: nmap --script default-* [target]
- Authentication bypass techniques
- Privilege escalation pathways

RISK ASSESSMENT MATRIX:
Classify findings using:
- CRITICAL: Remote code execution, authentication bypass, data exposure
- HIGH: Default credentials, outdated services with known exploits
- MEDIUM: Information disclosure, weak encryption, misconfiguration
- LOW: Version disclosure, verbose errors, unnecessary services

ATTACK SURFACE VISUALIZATION:
Create a mental model of:
- External attack surface
- Service interdependencies
- Trust relationships between services
- Potential pivot points
- Data flow patterns

DEFENSIVE RECOMMENDATIONS:
For each vulnerability provide:
- Immediate mitigation steps
- Long-term remediation strategies
- Compensating controls
- Detection and monitoring rules
- Hardening guidelines specific to the service

ADVANCED TOOLCHAIN INTEGRATION:
Suggest complementary tools:
- Web: SQLmap, wfuzz, gobuster, feroxbuster
- Network: masscan, zmap, unicornscan
- Exploitation: Metasploit modules, searchsploit queries
- Custom scripts: Python/Bash examples for specific scenarios

OUTPUT STRUCTURE:
Organize findings by:
1. Executive Summary (critical findings first)
2. Host-by-host detailed analysis
3. Service-specific vulnerability chains
4. Prioritized remediation roadmap
5. Red team exercise scenarios
6. Blue team detection opportunities
7. Compliance implications (PCI-DSS, HIPAA, etc.)

LEARNING OBJECTIVES:
For each finding, include:
- Why this matters in real-world attacks
- Historical breaches exploiting similar vulnerabilities
- Hands-on lab exercises to reproduce findings
- Defensive coding/configuration practices
- Relevant security research papers or advisories

Provide your analysis with the precision of a professional penetration test report while maintaining educational value. Include command examples that can be directly executed, explain the underlying protocols and vulnerabilities, and connect findings to the broader security landscape.

Analyze the following Nmap scan output:
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
elif len(sys.argv) > 2:
    print("="*60)
    print(f"{RED}ERROR: Invalid arguments!{RESET}")
    print("Usage:")
    print("  Learn-Nmap.py <Host or Network>")
    print("  Learn-Nmap.py  (no arguments)")
    print("="*60)
    sys.exit(1)
else:
    print(intro)
    target = input("Enter target (IP/Network): ")

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
report_file = "ollama_summary.txt"
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

