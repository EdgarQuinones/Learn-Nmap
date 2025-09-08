import os
import subprocess
import xml.etree.ElementTree as ET
import sys
import time 

# ANSI color codes
RED = "\033[91m"      # Closed / filtered / errors
GREEN = "\033[92m"    # Open ports
YELLOW = "\033[93m"   # Host headers / summary labels
CYAN = "\033[96m"     # Intro / summary headers
RESET = "\033[0m"

# Subprocess variables
xml_file = "output.xml"
model = "llama3.1:8b"
from prompt import prompt

# Debug mode
debug = False

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
elif len(sys.argv) == 3 and sys.argv[2] == '-d':
    print("Debug mode enabled.")
    debug = True
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
        "ollama", "run", model,
        f"{prompt} {nmap_output}"
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

