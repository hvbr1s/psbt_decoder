#!/usr/bin/env python3

import sys
import subprocess
import base64

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <hex_psbt>")
    sys.exit(1)

hex_psbt = sys.argv[1].lower()

# Strip the "0x" prefix if present
if hex_psbt.startswith("0x"):
    hex_psbt = hex_psbt[2:]

# Convert from hex to binary
binary_psbt = bytes.fromhex(hex_psbt)

# Encode that binary data into base64
base64_psbt = base64.b64encode(binary_psbt).decode()

# Decode the PSBT with bitcoin-cli
try:
    result = subprocess.check_output(["bitcoin-cli", "decodepsbt", base64_psbt])
    print(result.decode())
except FileNotFoundError:
    print("Error: bitcoin-cli not found. Make sure Bitcoin Core is installed and on your PATH.")
except subprocess.CalledProcessError as e:
    print(f"Error running 'bitcoin-cli decodepsbt': {e}")