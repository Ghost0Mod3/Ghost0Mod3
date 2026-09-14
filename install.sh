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

python3 -m pip install \
    --break-system-packages \
    -r requirements.txt

echo ""
echo "Setting permissions..."

chmod +x launch_Ghost0Mod3.sh
chmod +x shutdown_Ghost0Mod3.sh
chmod +x install_desktop_launcher.sh

echo ""
echo "Installing desktop launchers..."

./install_desktop_launcher.sh

echo ""
echo "==================================="
echo "Ghost0Mod3 Installation Complete"
echo "==================================="

echo ""
echo "Desktop shortcuts created."
echo ""
echo "Launch using:"
echo "  Ghost0Mod3.desktop"
echo ""
echo "Or:"
echo "  ./launch_Ghost0Mod3.sh"
echo ""
