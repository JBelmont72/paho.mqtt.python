'''7 March 2025
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
import paho.mqtt.client as mqtt  

broker = "broker.hivemq.com"  
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
