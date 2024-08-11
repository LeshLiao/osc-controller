import socket
import time

# Set the IP address and port of the Pico
PICO_IP = '172.20.10.3'  # Replace with the IP address of your Pico
PICO_PORT = 5005

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send data
def send_data(data):
    sock.sendto(data, (PICO_IP, PICO_PORT))
    print(f'Sent: {data}')

# Test data
test_data_A = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x00\x00'  # Data to turn relay on
test_data_B = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x42\x00\x00\x00'  # Data to turn relay off

try:
    while True:
        send_data(test_data_A)
        time.sleep(2)
        send_data(test_data_B)
        time.sleep(2)

except KeyboardInterrupt:
    print("Test stopped by user.")
    sock.close()
