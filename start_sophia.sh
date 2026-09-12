#!/bin/bash

cd /home/main/SSID-Radar

# Put wlan1 into monitor mode
ip link set wlan1 down
iw dev wlan1 set type monitor
ip link set wlan1 up

# Launch Sophia
python3 sophia.py --iface wlan1 --host 127.0.0.1 --port 5000
