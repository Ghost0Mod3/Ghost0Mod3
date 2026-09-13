#!/bin/bash

pkill -f sophia.py

ip link set wlan1 down
iw dev wlan1 set type managed
ip link set wlan1 up

systemctl restart NetworkManager
