#!/usr/bin/env bash

echo "Stopping Ghost0Mod3..."

pkill -f "python3 main.py" || true

echo "Ghost0Mod3 stopped."
