#!/bin/bash

# ================================
# Learn-Nmap Setup Script for Linux
# ================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
model_name='mistral:7b-instruct'

echo "=========================================="
echo "    Learn-Nmap Setup Script for Linux     "
echo "=========================================="

# ------------------------------
# Helper Functions
# ------------------------------

# Check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect OS type
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            echo "debian"
        elif [ -f /etc/redhat-release ]; then
            echo "redhat"
        elif [ -f /etc/arch-release ]; then
            echo "arch"
        else
            echo "unknown"
        fi
    else
        echo "unknown"
    fi
}

OS_TYPE=$(detect_os)
echo -e "${YELLOW}Detected OS: $OS_TYPE${NC}"

# ------------------------------
# Install Nmap
# ------------------------------
echo -e "\n${YELLOW}Checking Nmap installation...${NC}"
if command_exists nmap; then
    echo -e "${GREEN}Nmap is already installed${NC}"
else
    echo -e "${YELLOW}Installing Nmap...${NC}"
    case $OS_TYPE in
        debian)
            sudo apt-get update
            sudo apt-get install -y nmap curl wget
            ;;
        redhat)
            sudo yum install -y nmap curl wget
            ;;
        arch)
            sudo pacman -S --noconfirm nmap curl wget
            ;;
        *)
            echo -e "${RED}Please install Nmap manually for your distribution${NC}"
            ;;
    esac
fi

# ------------------------------
# Install Python3 and pip
# ------------------------------
echo -e "\n${YELLOW}Checking Python3 installation...${NC}"
if command_exists python3; then
    echo -e "${GREEN}Python3 is already installed${NC}"
else
    echo -e "${YELLOW}Installing Python3...${NC}"
    case $OS_TYPE in
        debian)
            sudo apt-get install -y python3 python3-pip
            ;;
        redhat)
            sudo yum install -y python3 python3-pip
            ;;
        arch)
            sudo pacman -S --noconfirm python python-pip
            ;;
        *)
            echo -e "${RED}Please install Python3 manually for your distribution${NC}"
            ;;
    esac
fi

# ------------------------------
# Install Ollama
# ------------------------------
echo -e "\n${YELLOW}Checking Ollama installation...${NC}"
if command_exists ollama; then
    echo -e "${GREEN}Ollama is already installed${NC}"
else
    echo -e "${YELLOW}Installing Ollama...${NC}"
    curl -fsSL https://ollama.ai/install.sh | sh
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to install Ollama via official script. Trying alternative...${NC}"
        wget https://github.com/ollama/ollama/releases/latest/download/ollama-linux-amd64
        sudo mv ollama-linux-amd64 /usr/local/bin/ollama
        sudo chmod +x /usr/local/bin/ollama
    fi
fi

# ------------------------------
# Start Ollama service
# ------------------------------
echo -e "\n${YELLOW}Starting Ollama service...${NC}"
if command_exists systemctl && systemctl is-active --quiet ollama; then
    echo -e "${GREEN}Ollama service is already running${NC}"
else
    nohup ollama serve > /dev/null 2>&1 &
    sleep 3
    echo -e "${GREEN}Ollama is now running in the background${NC}"
fi

# ------------------------------
# Pull Llama 3.1 8B Model
# ------------------------------
echo -e "\n${YELLOW}Pulling $model_name model (this may take a while)...${NC}"
if command_exists ollama; then
    ollama pull llama3.1:8b
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Model downloaded successfully${NC}"
    else
        echo -e "${RED}Failed to download model. Please run 'ollama pull mistral:7b-instruct' manually${NC}"
    fi
else
    echo -e "${RED}Ollama not found. Cannot pull model.${NC}"
fi

# ------------------------------
# Make Learn-Nmap.py executable
# ------------------------------
if [ -f "Learn-Nmap.py" ]; then
    chmod +x Learn-Nmap.py
    echo -e "\n${GREEN}Learn-Nmap.py is now executable${NC}"
fi

# ------------------------------
# Finish
# ------------------------------
echo -e "\n=========================================="
echo -e "${GREEN}Setup Complete!${NC}"
echo -e "You can now run: ${YELLOW}python3 Learn-Nmap.py <target>${NC}"
echo -e "=========================================="