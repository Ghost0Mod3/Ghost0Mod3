#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

START_DESKTOP_FILE="$HOME/Desktop/Ghost0Mod3.desktop"
STOP_DESKTOP_FILE="$HOME/Desktop/Ghost0Mod3 Shutdown.desktop"

mkdir -p "$HOME/Desktop"

chmod +x "$SCRIPT_DIR/launch_Ghost0Mod3.sh"
chmod +x "$SCRIPT_DIR/shutdown_Ghost0Mod3.sh"

cat > "$START_DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=Ghost0Mod3
Comment=Launch Ghost0Mod3 Wi-Fi Radar
Exec=$SCRIPT_DIR/launch_Ghost0Mod3.sh
Path=$SCRIPT_DIR
Terminal=true
Categories=Network;Security;
EOF

cat > "$STOP_DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=Ghost0Mod3 Shutdown
Comment=Stop Ghost0Mod3
Exec=$SCRIPT_DIR/shutdown_Ghost0Mod3.sh
Path=$SCRIPT_DIR
Terminal=true
Categories=Network;Security;
EOF

chmod +x "$START_DESKTOP_FILE"
chmod +x "$STOP_DESKTOP_FILE"

if command -v gio >/dev/null 2>&1; then
    gio set "$START_DESKTOP_FILE" metadata::trusted true || true
    gio set "$STOP_DESKTOP_FILE" metadata::trusted true || true
fi

echo ""
echo "Created:"
echo "  $START_DESKTOP_FILE"
echo "  $STOP_DESKTOP_FILE"
echo ""
echo "Ghost0Mod3 desktop launchers installed."
