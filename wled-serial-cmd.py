import serial
import json
import time

# Replace '/dev/serial0' with the correct UART1 device if different
UART_PORT = "/dev/serial0"
BAUD_RATE = 115200  # Set the baud rate to match the ESP32

# Open the serial port
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)

# Function to send a JSON message to the ESP32
def send_json_message(data):
    try:
        # Convert Python dictionary to JSON string
        json_data = json.dumps(data)
        # Send JSON string over serial to the ESP32
        ser.write((json_data).encode())
        print(f"Sent: {json_data}")
    except Exception as e:
        print(f"Error sending JSON: {e}")

# Function to read a JSON message from the ESP32
def read_json_message():
    try:
        # Read data from the ESP32
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').strip()
            # Parse the message as JSON
            json_data = json.loads(message)
            print(f"Received: {json_data}")
            return json_data
    except json.JSONDecodeError:
        print("Received non-JSON data.")
    except Exception as e:
        print(f"Error reading JSON: {e}")
    return None

# Example usage
if __name__ == "__main__":
    try:
        # Wait for serial communication to establish
        time.sleep(2)

        # Example data to send (as a dictionary)
        data_to_send = {
            "on": "t",
            "v": True
             }

        # Send JSON data to ESP32
        send_json_message(data_to_send)

        # Read JSON message from ESP32
        while True:
            received_data = read_json_message()
            if received_data:
                # Handle received data
                break
            time.sleep(1)  # Add a small delay between reads

    except KeyboardInterrupt:
        print("Terminating script.")
    finally:
        print("end of script.")
        ser.close()  # Close the serial port on exit
