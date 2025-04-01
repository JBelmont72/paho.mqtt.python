'''
the pico server with the led is 'led_mqtt_server.py' in this folder
'''
import paho.mqtt.client as mqtt

# MQTT Settings
# BROKER = "broker.hivemq.com"    # Public broker this is the publisher client python
BROKER = "test.mosquitto.org"    # Public broker this is the publisher client python
TOPIC = "led/control"           # Same topic as the subscriber

# Create an MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(BROKER, 1883, 60)

# Send ON or OFF command
def control_led(command):
    if command.upper() == "ON" or command.upper() == "OFF":
        client.publish(TOPIC, command)
        print(f"Sent command: {command}")
    else:
        print("Invalid command. Use 'ON' or 'OFF'.")

# Example usage
while True:
    command = input("Enter LED command (ON/OFF or 'exit' to quit): ").strip().upper()
    if command == "EXIT":
        print("Exiting...")
        break
    control_led(command)

client.disconnect()


# control_led("ON")   # Turn LED ON
# control_led("OFF")  # Turn LED OFF

# Disconnect
client.disconnect()
