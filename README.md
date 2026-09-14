# Ghost0Mod3

Ghost0Mod3 is a Raspberry Pi based Wi-Fi reconnaissance and network awareness platform built around Scapy, monitor mode capture, and a lightweight Tkinter user interface.

The project is designed to run on a Raspberry Pi 4 with a dedicated wireless adapter operating in monitor mode.

---

## Features

- Live Wi-Fi network discovery
- Monitor mode packet capture
- Real-time network list
- Network classification
- RSSI tracking
- Target selection
- Target persistence
- Channel hopping
- Raspberry Pi optimized deployment
- Desktop launcher integration

---

## Hardware

Recommended:

- Raspberry Pi 4
- External Wi-Fi adapter with monitor mode support
- 7" Raspberry Pi display
- Vehicle-mounted or portable power source

Tested with:

- wlan0 for management
- wlan1 for monitor mode capture

---

## Project Structure

```text
Ghost0Mod3
│
├── core/
│   ├── channel_hopper.py
│   ├── classifier.py
│   ├── packet_parser.py
│   ├── scanner.py
│   └── target_manager.py
│
├── gui/
│   └── dashboard.py
│
├── data/
│
├── tests/
│   ├── test_async.py
│   ├── test_beacons.py
│   └── test_scapy.py
│
├── legacy/
│
├── main.py
├── requirements.txt
└── VERSION
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ghost0Mod3/Ghost0Mod3.git
cd Ghost0Mod3
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

Launch manually:

```bash
sudo -E python3 main.py
```

---

## Desktop Launchers

Install desktop launchers:

```bash
chmod +x install_desktop_launcher.sh
./install_desktop_launcher.sh
```

This creates:

```text
Ghost0Mod3.desktop
Ghost0Mod3 Shutdown.desktop
```

on the Raspberry Pi desktop.

---

## Monitor Mode

Verify monitor mode:

```bash
iw dev
```

Expected:

```text
Interface wlan1
type monitor
```

---

## Target Tracking

Ghost0Mod3 supports:

- Selecting a target network
- Saving a target
- Reloading previously selected targets

Target information is stored in:

```text
data/target.json
```

---

## Legacy Components

The original SOPHIA application and associated launcher files have been archived under:

```text
legacy/
```

These files are preserved for reference but are not part of the active Ghost0Mod3 application.

---

## Status

Current Phase:

```text
Alpha
```

Working:


- Packet capture
- Monitor mode
- Channel hopping
- Classification
- Target management
- Raspberry Pi deployment
- Desktop launchers
## Supported Operating Systems

Officially Tested:

- Raspberry Pi OS


Expected Compatibility:

- Debian
- Ubuntu
- Linux Mint
- Kali Linux

Not Supported:

- Windows
- macOS

Ghost0Mod3 relies on:

- Python 3
- Scapy
- Linux monitor mode support
- aircrack-ng
- iw
- wireless-tools
Planned:

- Improved target panel
- Radar audio notifications
- Confidence scoring
- Distance estimation
- Vehicle deployment profile

  ------------------------------------------------------
  ## Disclaimer
--------------------
Ghost0Mod3 is intended solely for educational, research, network analysis,
and authorized security testing purposes.

Users are responsible for ensuring that their use of this software complies
with all applicable local, state, federal, and international laws.

The author assumes no responsibility and accepts no liability for any misuse,
unauthorized access, criminal activity, damages, or legal
consequences resulting from the use of this software.

Use at your own risk.
