#!/usr/bin/python3

import serial
import json
import sys
import os

# Validate arguments
if len(sys.argv) < 4:
    print("Usage: wled-serial-cmd.py <retrosys> <emul> <romfile> [state]")
    sys.exit(1)

retrosys = sys.argv[1].upper()  # Convert retrosys to uppercase
emul = sys.argv[2]
romfile = sys.argv[3]

# Extract only the filename without extension
romfile = os.path.basename(romfile)  # Get filename from full path
romfile = os.path.splitext(romfile)[0]  # Remove the extension

# File path
json_file_path = "/tmp/current-rom.txt"

# Create JSON data
json_data = {"seg": [{"id": 0, "n": retrosys}, {"id": 1, "n": romfile}]}

# Write and Read JSON in a Single Operation
with open(json_file_path, "w+") as out:
    json.dump(json_data, out)
    out.seek(0)  # Move cursor to the beginning
    jsonfile = json.load(out)  # Read it back

#print(jsonfile)

def send_json_to_wled(ser, json_data):
    """Sends JSON data to WLED over serial."""
    ser.write((json.dumps(json_data) + '\n').encode())
    #print("Sent to WLED:", json_data)

def read_json_from_wled(ser):
    """Reads JSON data from WLED over serial."""
    line = ser.readline().decode().strip()
    return json.loads(line) if line else {}

def get_current_state(ser):
    """Gets and prints the current WLED state."""
    send_json_to_wled(ser, {"v": True})
    state = read_json_from_wled(ser)
    print("Current state:", state)
    return state

# Open serial connection with error handling
try:
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)  # Adjust timeout as needed
except serial.SerialException as e:
    print(f"Serial Error: {e}")
    sys.exit(1)

# Check if "state" argument is passed
if len(sys.argv) > 4 and sys.argv[4].lower() == "state":
    get_current_state(ser)
    sys.exit(0)  # Exit after fetching state

# Send correct JSON data to WLED
send_json_to_wled(ser, jsonfile)
