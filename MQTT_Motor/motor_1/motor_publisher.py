'''7 March 2025 this is the first test motor/control message publisher and pico subscriber
Broker: The server that handles messages (hivemq in this case)
Topic: The channel where messages are sent (motor/control)
Message: What you want to send (e.g., "Turn Motor ON")
Connect, publish, disconnect: Basic steps to send data!
In my PythonTeacher folder
GREAT TUTORIAL  https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
Discusses changes in MQTT:

https://www.emqx.com/en/blog/introduction-to-mqtt-5
https://eclipse.dev/paho/files/paho.mqtt.python/html/migrations.html

http://www.steves-internet-guide.com/mqtt-works/

very helpful and direct reference: https://www.hivemq.com/blog/implementing-mqtt-in-python/
'''
import paho.mqtt.client as mqtt  ## publishes in python editor and Client
broker ='test.mosquitto.org'
# broker = "broker.hivemq.com"  
port = 1883  
topic = "motor/control"  

# Create an MQTT client  
client = mqtt.Client()  
# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  

# Connect to the broker  
client.connect(broker, port, 60)  

# Publish a message  
client.publish(topic, "Turn Motor ON")  
print(f"Message sent to topic '{topic}'")  

# Disconnect  
client.disconnect()
######## below is the PicoW subscriber & the server
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
