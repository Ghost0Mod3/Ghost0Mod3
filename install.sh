#!/usr/bin/env bash

set -e

echo "==================================="
echo "Ghost0Mod3 Installer"
echo "==================================="

echo ""
echo "Updating system..."

sudo apt update
sudo apt upgrade -y

echo ""
echo "Installing Linux dependencies..."

sudo apt install -y \
    git \
    python3 \
    python3-pip \
    python3-tk \
    python3-venv \
    aircrack-ng \
    iw \
    wireless-tools

echo ""
echo "Installing Python dependencies..."

sudo python3 -m pip install \
    --break-system-packages \
    -r requirements.txt

echo ""
echo "Setting executable permissions..."

chmod +x launch_Ghost0Mod3.sh

chmod +x shutdown_Ghost0Mod3.sh

if [ -f install_desktop_launcher.sh ]; then
    chmod +x install_desktop_launcher.sh
fi

echo ""
echo "Installing desktop launchers..."

if [ -f install_desktop_launcher.sh ]; then
    ./install_desktop_launcher.sh
fi

echo ""
echo "Verifying installation..."

python3 --version

echo ""
echo "Checking Scapy installation..."

python3 -c "from scapy.all import *; print('Scapy OK')" || true

echo ""
echo "==================================="
echo "Ghost0Mod3 Installation Complete!"
echo "==================================="

echo ""
echo "Next Steps:"
echo ""
echo "1. Configure monitor mode:"
echo "   sudo ip link set wlan1 down"
echo "   sudo iw dev wlan1 set type monitor"
echo "   sudo ip link set wlan1 up"
echo ""
echo "2. Verify:"
echo "   iw dev wlan1 info"
echo ""
echo "   Expected:"
echo "   type monitor"
echo ""
echo "3. Launch Ghost0Mod3:"
echo "   ./launch_Ghost0Mod3.sh"
echo ""
