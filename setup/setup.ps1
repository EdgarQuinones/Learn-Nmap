# Learn-Nmap Setup Script for Windows (PowerShell)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "    Learn-Nmap Setup Script for Windows   " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Check for administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script requires Administrator privileges." -ForegroundColor Red
    Write-Host "Please run PowerShell as Administrator." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Function to check if a command exists
function Test-CommandExists {
    param($command)
    $null = Get-Command $command -ErrorAction SilentlyContinue
    return $?
}

# Check Python
Write-Host "`nChecking Python installation..." -ForegroundColor Yellow
if (Test-CommandExists python) {
    Write-Host "Python is installed" -ForegroundColor Green
} else {
    Write-Host "Python is not installed!" -ForegroundColor Red
    Write-Host "Downloading Python installer..." -ForegroundColor Yellow
    
    $pythonUrl = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
    $pythonInstaller = "$env:TEMP\python-installer.exe"
    
    Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller
    Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet", "PrependPath=1" -Wait
    Remove-Item $pythonInstaller
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Check Nmap
Write-Host "`nChecking Nmap installation..." -ForegroundColor Yellow
if (Test-CommandExists nmap) {
    Write-Host "Nmap is installed" -ForegroundColor Green
} else {
    Write-Host "Nmap is not installed!" -ForegroundColor Red
    Write-Host "Downloading Nmap installer..." -ForegroundColor Yellow
    
    $nmapUrl = "https://nmap.org/dist/nmap-7.94-setup.exe"
    $nmapInstaller = "$env:TEMP\nmap-setup.exe"
    
    Invoke-WebRequest -Uri $nmapUrl -OutFile $nmapInstaller
    Start-Process -FilePath $nmapInstaller -Wait
    Remove-Item $nmapInstaller
}

# Check Ollama
Write-Host "`nChecking Ollama installation..." -ForegroundColor Yellow
if (Test-CommandExists ollama) {
    Write-Host "Ollama is installed" -ForegroundColor Green
} else {
    Write-Host "Ollama is not installed!" -ForegroundColor Red
    Write-Host "Downloading Ollama installer..." -ForegroundColor Yellow
    
    $ollamaUrl = "https://ollama.ai/download/OllamaSetup.exe"
    $ollamaInstaller = "$env:TEMP\OllamaSetup.exe"
    
    Invoke-WebRequest -Uri $ollamaUrl -OutFile $ollamaInstaller
    Start-Process -FilePath $ollamaInstaller -Wait
    Remove-Item $ollamaInstaller
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Start Ollama service
Write-Host "`nStarting Ollama service..." -ForegroundColor Yellow
$ollamaProcess = Get-Process ollama -ErrorAction SilentlyContinue
if ($null -eq $ollamaProcess) {
    Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 5
    Write-Host "Ollama service started" -ForegroundColor Green
} else {
    Write-Host "Ollama service is already running" -ForegroundColor Green
}

# Pull the model
Write-Host "`nPulling Llama 3.1 8B model (this may take a while)..." -ForegroundColor Yellow
Write-Host "This will download approximately 4.7GB of data" -ForegroundColor Yellow
& ollama pull llama3.1:8b

if ($LASTEXITCODE -eq 0) {
    Write-Host "Model downloaded successfully" -ForegroundColor Green
} else {
    Write-Host "Failed to download model" -ForegroundColor Red
    Write-Host "Please run 'ollama pull llama3.1:8b' manually" -ForegroundColor Red
}

Write-Host "`n==========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "You can now run: python Learn-Nmap.py [target]" -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Cyan
Read-Host "Press Enter to exit"