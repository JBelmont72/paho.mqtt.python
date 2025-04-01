'''
will need to upload Motor_Class.py to pico 
this is the server subscriber pico
'''
import network
import time
from machine import Pin, PWM
from umqtt.simple import MQTTClient
from Motor_Class import MotorController

# Wi-Fi and MQTT Settings
SSID = "Your_WiFi_SSID"
PASSWORD = "Your_WiFi_Password"
# BROKER = "broker.hivemq.com"
BROKER = "test.mosquitto.org"
TOPIC = "robot/control"

# Motor pins for Kitronik Robot Platform
motor_pins = {
    'motor1': {'forward': 20, 'reverse': 19},  # Left motor
    'motor2': {'forward': 6, 'reverse': 7}    # Right motor
}

# Create motor controller object
robot = MotorController(motor_pins['motor1'], motor_pins['motor2'])

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# MQTT message handler
def on_message(topic, msg):
    message = msg.decode().strip()
    print(f"Received message: {message}")

    if message.startswith("FORWARD"):
        speed = int(message.split(",")[1]) if "," in message else 50
        robot.move_forward(speed)

    elif message.startswith("BACKWARD"):
        speed = int(message.split(",")[1]) if "," in message else 50
        robot.move_backward(speed)

    elif message.startswith("LEFT"):
        speed = int(message.split(",")[1]) if "," in message else 50
        robot.turn_left(speed)

    elif message.startswith("RIGHT"):
        speed = int(message.split(",")[1]) if "," in message else 50
        robot.turn_right(speed)

    elif message == "STOP":
        robot.stop()

# Connect to MQTT broker
def start_mqtt():
    client = MQTTClient("motor_server", BROKER)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(TOPIC)
    print(f"Subscribed to topic '{TOPIC}'")

    while True:
        client.wait_msg()

# Main program
connect_wifi()
start_mqtt()
