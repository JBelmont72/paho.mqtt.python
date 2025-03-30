
 ++led_mqtt_server.py this is the pico server subscriber to the led_publisher.py with the leds connected
++ motor_MicroSubscriber.py    python teacher-AI. march 25,25  mircopython pico dc motor subscriber
++ motor_PythonSubscriber.py  This is subscribing on Python Not on a pico
++ motor_publisher.py This is publishing  on Python Not on a pico

7 March 2025
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