'''Using UDP to send servo commands from python client to the PicoW server!
Client Side Changes:
Send specific servo angle data (e.g., ANGLE:90).
Wait for acknowledgment from the Pico W after sending.
Control the time interval dynamically.
Server Side Changes:
Decode and parse the received data to extract the angle.
Move the servo to the requested angle.
Send an acknowledgment back to the client.
below I have four programs:
1-python client code ('utf_8')
2-PicoW server code ('utf-8')
3-python client struct
4-PicoW server code (struct)
At bottom is discussion of code versus struct 
'''
import socket
import time

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.223', 12345)  # Update with your Pico W IP address

# Control loop
while True:
    angle = input("Enter servo angle (0-180) or 'exit' to quit: ")
    
    if angle.lower() == 'exit':
        print("Exiting...")
        break
    
    try:
        angle_int = int(angle)
        if 0 <= angle_int <= 180:
            message = f"ANGLE:{angle_int}"
            client_socket.sendto(message.encode(), server_address)
            
            # Receive acknowledgment from server
            data, addr = client_socket.recvfrom(1024)
            print('Acknowledgment from server:', data.decode())
            
            # Set delay dynamically if needed
            delay = int(input("Enter delay time in seconds before next command: "))
            time.sleep(delay)
        else:
            print("Angle must be between 0 and 180.")
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")

client_socket.close()
###########~~~~ number 2 below is the PicoW server code with servo
# import network
# import usocket as socket
# import secrets
# import time
# from machine import Pin, PWM

# # WiFi setup
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(secrets.ssid_condo, secrets.password_condo)

# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("WiFi connected, IP:", wlan.ifconfig()[0])

# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("UDP server is listening...")

# # Servo setup
# servo_pin = Pin(15)  # Update with your servo pin
# servo = PWM(servo_pin)
# servo.freq(50)  # 50 Hz for typical servos

# # Function to set servo angle
# def set_servo_angle(angle):
#     # Convert angle (0-180) to duty cycle (1000-9000 for Pico PWM)
#     duty = int(1000 + (angle / 180) * 8000)
#     servo.duty_u16(duty)
#     time.sleep(0.5)

# # Listen for incoming requests
# while True:
#     print("Waiting for request...")
#     request, client_address = server_socket.recvfrom(1024)
#     message = request.decode()
    
#     if message.startswith("ANGLE:"):
#         try:
#             angle = int(message.split(":")[1])
#             if 0 <= angle <= 180:
#                 set_servo_angle(angle)
#                 response = f"Servo moved to {angle} degrees"
#             else:
#                 response = "Invalid angle range. Must be 0-180."
#         except ValueError:
#             response = "Invalid angle format."
#     else:
#         response = "Unknown command."
    
#     # Send acknowledgment back to the client
#     server_socket.sendto(response.encode(), client_address)
#     print(f"Acknowledgment sent to {client_address}")
#####~~~~~ below is #3 client code on python text editor, sending in binary STRUCT
# import socket
# import struct
# import time

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.1.223', 12345)

# while True:
#     angle = input("Enter servo angle (0-180) or 'exit' to quit: ")
    
#     if angle.lower() == 'exit':
#         print("Exiting...")
#         break
    
#     try:
#         angle_int = int(angle)
#         if 0 <= angle_int <= 180:
#             # Pack angle into 2-byte binary format
#             message = struct.pack('!H', angle_int)
#             client_socket.sendto(message, server_address)
            
#             # Receive acknowledgment
#             data, addr = client_socket.recvfrom(1024)
#             print('Acknowledgment from server:', data.decode())
            
#             delay = int(input("Enter delay time in seconds: "))
#             time.sleep(delay)
#         else:
#             print("Angle must be between 0 and 180.")
#     except ValueError:
#         print("Invalid input. Please enter a number or 'exit'.")
########~~~~  #4 is the picoW server UDP with STRUCT receiving in binary code
# import network
# import usocket as socket
# import secrets
# import struct
# import time
# from machine import Pin, PWM

# # WiFi setup
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(secrets.ssid_condo, secrets.password_condo)

# while not wlan.isconnected():
#     time.sleep(1)
# print("WiFi connected, IP:", wlan.ifconfig()[0])

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("UDP server listening...")

# servo_pin = Pin(15)
# servo = PWM(servo_pin)
# servo.freq(50)

# def set_servo_angle(angle):
#     duty = int(1000 + (angle / 180) * 8000)
#     servo.duty_u16(duty)
#     time.sleep(0.5)

# while True:
#     print("Waiting for request...")
#     request, client_address = server_socket.recvfrom(1024)
    
#     try:
#         # Unpack binary angle value
#         angle = struct.unpack('!H', request)[0]
#         if 0 <= angle <= 180:
#             set_servo_angle(angle)
#             response = f"Servo moved to {angle} degrees"
#         else:
#             response = "Invalid angle range"
#     except struct.error:
#         response = "Error decoding data"
    
#     # Send acknowledgment
#     server_socket.sendto(response.encode(), client_address)
#     print(f"Acknowledgment sent to {client_address}")










###~~~~~~~~~
'''advantages and disadvantages of struct
struct converts data to binary format, which is more compact and faster to transmit than plain text.
Ideal for sending numbers, sensor data, or servo angles that don’t require human readability.
✅ Consistent Data Size:
Binary formats have a fixed size, making it easier to parse data reliably on the receiving end.
Useful when you need predictable data lengths, avoiding string parsing errors.
✅ Reduced Network Bandwidth:
Smaller packet sizes mean faster communication and lower network load, especially if you’re sending frequent updates (e.g., 100+ messages per second)
When to skip Struct:
When to Skip struct
❗ Simplicity and Debugging:
Text-based communication (e.g., ANGLE:90) is easier to debug and troubleshoot.
Easier to modify and test without worrying about encoding and decoding errors.
❗ Low Data Volume or Frequency:
If you’re only sending a few values at a time (like servo angles), the overhead of encoding/decoding with struct isn’t worth it.
The data size difference between sending b'\x5a' (binary) and b'ANGLE:90' (text) is negligible for infrequent messages.
comparison: Without struct (current text-based approach)
Message: "ANGLE:90"
Easier to debug and modify.
Slightly larger packets.
With struct (binary approach)
Message: struct.pack('!H', 90)
!H sends a 2-byte unsigned short in network byte order.
On the Pico: angle = struct.unpack('!H', request)[0]
Smaller and faster, but harder to debug or change.
'''
