#!/bin/bash

# Check if running on Kali Linux
if [ -f "/etc/debian_version" ]; then
    # Kali Linux installation
    sudo apt-get update
    sudo apt-get install -y python3-pip
elif [ -n "$(command -v termux-setup-storage)" ]; then
    # Termux installation
    pkg update
    pkg install -y python
else
    echo "Unsupported system. Please install required dependencies manually."
    exit 1
fi

# Install Python modules
pip install pyfiglet 
pip install phonenumbers

echo "Installation complete. Run 'python3 phone_zone.py' to use the Phone-Zone tool."
echo "if pyfiglet module is not installing please run pip install pyfiglet manually"
