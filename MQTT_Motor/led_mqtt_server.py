'''  this is the pico server with the leds connected'''
import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

# Wi-Fi and MQTT Settings
SSID = "Your_WiFi_SSID"         # Your Wi-Fi SSID
PASSWORD = "Your_WiFi_Password" # Your Wi-Fi password
BROKER = "broker.hivemq.com"    # Public MQTT broker
TOPIC = "led/control"           # MQTT topic for control messages

# Set up LED on Pin 16
led = Pin(16, Pin.OUT)
led.value(0)  # Start with LED OFF

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected to Wi-Fi. IP:", wlan.ifconfig()[0])

# Handle incoming MQTT messages
def on_message(topic, msg):
    message = msg.decode().strip()
    print(f"Received: {message}")

    if message == "ON":
        led.value(1)  # Turn LED ON
        print("LED turned ON")
    elif message == "OFF":
        led.value(0)  # Turn LED OFF
        print("LED turned OFF")
    else:
        print("Unknown command")

# Connect to MQTT broker
def start_mqtt():
    client = MQTTClient("led_server", BROKER)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(TOPIC)
    print(f"Subscribed to topic '{TOPIC}'")

    while True:
        client.wait_msg()

# Main Program
connect_wifi()
start_mqtt()
