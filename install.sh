#!/usr/bin/env bash

set -e

echo "Updating system..."

sudo apt update
sudo apt upgrade -y

echo "Installing system dependencies..."

sudo apt install -y \
    git \
    python3 \
    python3-pip \
    aircrack-ng \
    iw \
    wireless-tools

echo "Installing Python dependencies..."

pip3 install -r requirements.txt

echo "Installation complete."
