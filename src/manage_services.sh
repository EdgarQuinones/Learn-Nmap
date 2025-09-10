#!/bin/bash
# Usage: ./manage_services.sh start
#        ./manage_services.sh stop
# Starts or stops services for Nmap testing

ACTION=$1

if [[ "$ACTION" != "start" && "$ACTION" != "stop" ]]; then
    echo "Usage: $0 [start|stop]"
    exit 1
fi

# List of services
SERVICES=("apache2" "ssh" "vsftpd" "mysql")

for service in "${SERVICES[@]}"; do
    echo "[*] $ACTION $service..."

    # Special handling for SSH (service + socket)
    if [[ "$service" == "ssh" && "$ACTION" == "stop" ]]; then
        sudo systemctl stop ssh.service ssh.socket 2>/dev/null
        sudo systemctl disable ssh.service ssh.socket 2>/dev/null
    else
        sudo systemctl $ACTION $service 2>/dev/null
        if [[ "$ACTION" == "stop" ]]; then
            sudo systemctl disable $service 2>/dev/null
        fi
    fi
done

echo -e "[*] Services $ACTION completed!\n"

# Run nmap scan
nmap localhost
