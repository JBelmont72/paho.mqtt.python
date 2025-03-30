'''motor_publisher.py has the matching python client publisher and this is the 
motor_MicropythonSubscriber.py server on picow  
These just to set up the send and receive of a command. No action except messages
python teacher. march 25,25  mircopython pico dc motor subscriber
'''
import network
import time
import secrets
from umqtt.simple import MQTTClient
from machine import Pin

# Wi-Fi and MQTT settings

SSID = secrets.ssid_condo
PASSWORD = secrets.password_condo
BROKER = "test.mosquitto.org"

#BROKER = "broker.hivemq.com"
TOPIC = "motor/control"

# Set up the motor pin (GPIO 15 for example)
motor = Pin(0, Pin.OUT)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected to WiFi!")

# Handle incoming messages
def on_message(topic, msg):
    print(f"Received message on topic: {topic.decode()}")
    print(f"Message content: {msg.decode()}")

    print(f"Received message: {msg.decode()}")
    if msg.decode() == "Turn Motor ON":
        motor.value(1)  # Turn the motor on
        print("Motor turned ON")
    elif msg.decode() == "Turn Motor OFF":
        motor.value(0)  # Turn the motor off
        print("Motor turned OFF")

# Connect to MQTT and listen for messages
def connect_mqtt():
    client = MQTTClient("pico_client", BROKER)
    client.set_callback(on_message)
    client.connect()
    print("Connected to MQTT Broker!")
    print(f"Subscribed to {TOPIC}")

    client.subscribe(TOPIC)
    print(f"Subscribed to topic {TOPIC}")
    while True:
        try:
            client.wait_msg()
        except Exception as e:
            print(f"Error: {e}")


# Run the program
connect_wifi()
connect_mqtt()
