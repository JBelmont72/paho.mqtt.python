'''
four programs for client on Python editor and server on PicoW
1. PicoW server encode/decode
2. Python client encode/decode
3. PicoW server STRUCT
4. Python client STRUCT binary coding
ping 192.168.1.29

print(wlan.ifconfig()) if ip 0.0.0.0 then not connected

'''
### #1 is the picoW server
# import network
# import usocket as socket
# import time
# import machine

# # LED setup
# greenLED = machine.Pin(16, machine.Pin.OUT)
# yellowLED = machine.Pin(18, machine.Pin.OUT)
# redLED = machine.Pin(17, machine.Pin.OUT)

# # Connect to Wi-Fi
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48', 'waterypanda914')

# while not wlan.isconnected():
#     time.sleep(1)

# print("Connection Completed")
# print('WiFi connected:', wlan.ifconfig())

# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])

# while True:
#     print('Waiting for a request from the client...')
    
#     # Receive client request
#     request, client_address = server_socket.recvfrom(1024)
#     print(f"Received raw data: {request}")

#     color = request.decode().strip()
    
#     print(f"Client Request: {color}")
#     print("FROM CLIENT:", client_address)

#     # Control LEDs based on the request
#     if color == "green":
#         greenLED.on()
#         yellowLED.off()
#         redLED.off()
#     elif color == "yellow":
#         greenLED.off()
#         yellowLED.on()
#         redLED.off()
#     elif color == "red":
#         greenLED.off()
#         yellowLED.off()
#         redLED.on()
#     elif color == "off":
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()
#     else:
#         print("Invalid command received")

#     # Send response to the client
#     response = f"LED {color} executed"
#     server_socket.sendto(response.encode(), client_address)
#     print(f'Sent data to {client_address}')
##########~~  #2 below is python client regular decode /encode
import socket

# Server details
SERVER_IP = '192.168.1.223'  # Replace with your Pico W's IP address
SERVER_PORT = 12345

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    command = input("Enter LED color (green, yellow, red, off): ").strip()
    
    if command not in {"green", "yellow", "red", "off"}:
        print("Invalid command. Please enter 'green', 'yellow', 'red', or 'off'.")
        continue

    # Send the command as a plain string
    client_socket.sendto(command.encode(), (SERVER_IP, SERVER_PORT))
    
    # Receive and decode response from server
    response, _ = client_socket.recvfrom(1024)
    print("Server Response:", response.decode())
    
# ####~~~ #3 below is picoW  server led control with Struct
# import network
# import usocket as socket
# import time
# import machine
# import struct

# # LED setup
# greenLED = machine.Pin(16, machine.Pin.OUT)
# yellowLED = machine.Pin(18, machine.Pin.OUT)
# redLED = machine.Pin(17, machine.Pin.OUT)

# # Connect to Wi-Fi
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48', 'waterypanda914')

# while not wlan.isconnected():
#     time.sleep(1)

# print("Connection Completed")
# print('WiFi connected:', wlan.ifconfig())

# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])

# while True:
#     print('Waiting for a request from the client...')
    
#     # Receive and unpack the client request
#     request, client_address = server_socket.recvfrom(1024)
### the next try except are to check for unpacking errors!
    ## length = len(request)
   # # try:
   ##     color = struct.unpack(f'{length}s', request)[0].decode().strip()
   # #     print(f"Unpacked Color: {color}")
    ## except struct.error as e:
    ##     print(f"Struct unpack error: {e}")



#     length = len(request)
#     color = struct.unpack(f'{length}s', request)[0].decode().strip()
    
#     print(f"Client Request: {color}")
#     print("FROM CLIENT:", client_address)

#     # Control LEDs
#     if color == "green":
#         greenLED.on()
#         yellowLED.off()
#         redLED.off()
#     elif color == "yellow":
#         greenLED.off()
#         yellowLED.on()
#         redLED.off()
#     elif color == "red":
#         greenLED.off()
#         yellowLED.off()
#         redLED.on()
#     elif color == "off":
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()

#     # Send response to client
#     response = f"LED {color} executed"
#     packed_response = struct.pack(f'{len(response)}s', response.encode())
#     server_socket.sendto(packed_response, client_address)
#     print(f'Sent data to {client_address}')



# ####~~~~~ #4 below is client on MAC in python with struct
# import socket
# import struct

# # Server details
# SERVER_IP = '192.168.1.29'  # Replace with your Pico W's IP address
# SERVER_PORT = 12345

# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     command = input("Enter LED color (green, yellow, red, off): ").strip()
    
#     if command not in {"green", "yellow", "red", "off"}:
#         print("Invalid command. Please enter 'green', 'yellow', 'red', or 'off'.")
#         continue

#     # Pack the command and send it
#     packed_command = struct.pack(f'{len(command)}s', command.encode())
#     client_socket.sendto(packed_command, (SERVER_IP, SERVER_PORT))
    
#     # Receive and unpack response from server
#     response, _ = client_socket.recvfrom(1024)
#     length = len(response)
#     unpacked_response = struct.unpack(f'{length}s', response)[0].decode()
#     print("Server Response:", unpacked_response)

