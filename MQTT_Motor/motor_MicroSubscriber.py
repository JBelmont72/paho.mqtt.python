'''
python teacher. march 25,25  mircopython pico dc motor subscriber
'''
import network
import time
import 
from umqtt.simple import MQTTClient
from machine import Pin
SSID=
# Wi-Fi and MQTT settings
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"
BROKER = "broker.hivemq.com"
TOPIC = "motor/control"

# Set up the motor pin (GPIO 15 for example)
motor = Pin(15, Pin.OUT)

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
    client.subscribe(TOPIC)
    print(f"Subscribed to topic {TOPIC}")

    while True:
        client.wait_msg()

# Run the program
connect_wifi()
connect_mqtt()
