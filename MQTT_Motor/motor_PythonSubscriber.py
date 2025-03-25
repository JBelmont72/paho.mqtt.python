'''7 March 2025
This is subscribing on Python Not on a pico
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

🟢 Explanation:
on_message: Handles incoming messages and prints them
subscribe: Listens for messages on the same topic as the publisher (motor/control)
loop_forever: Keeps the script running to listen for messages continuously
'''
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "motor/control"

# Define what happens when a message is received
def on_message(client, userdata, message):
    print(f"Received message: '{message.payload.decode()}' on topic '{message.topic}'")

# Create an MQTT client
client = mqtt.Client()

# Set up the callback function
client.on_message = on_message

# Connect to the broker and subscribe
client.connect(broker, port, 60)
client.subscribe(topic)

print(f"Subscribed to topic '{topic}' — waiting for messages...")

# Keep the connection alive
client.loop_forever()
