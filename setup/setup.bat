@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo     Learn-Nmap Setup Script for Windows
echo ==========================================

:: Check for administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrator privileges.
    echo Please run as Administrator.
    pause
    exit /b 1
)

:: Check if Python is installed
echo.
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed!
    echo Please download and install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
) else (
    echo Python is installed
)

:: Check if Nmap is installed
echo.
echo Checking Nmap installation...
nmap --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Nmap is not installed!
    echo.
    echo Downloading Nmap installer...
    :: Download Nmap using PowerShell
    powershell -Command "& {Invoke-WebRequest -Uri 'https://nmap.org/dist/nmap-7.94-setup.exe' -OutFile 'nmap-setup.exe'}"
    
    echo Installing Nmap...
    echo Please follow the installation wizard
    start /wait nmap-setup.exe
    
    :: Clean up installer
    del nmap-setup.exe
    
    :: Verify installation
    nmap --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Nmap installation failed or not added to PATH
        echo Please install Nmap manually from https://nmap.org/download.html
        pause
        exit /b 1
    )
) else (
    echo Nmap is installed
)

:: Check if Ollama is installed
echo.
echo Checking Ollama installation...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Ollama is not installed!
    echo.
    echo Downloading Ollama installer...
    
    :: Download Ollama for Windows
    powershell -Command "& {Invoke-WebRequest -Uri 'https://ollama.ai/download/OllamaSetup.exe' -OutFile 'OllamaSetup.exe'}"
    
    echo Installing Ollama...
    echo Please follow the installation wizard
    start /wait OllamaSe