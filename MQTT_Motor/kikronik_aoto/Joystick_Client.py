'''

Motor Pico W:
Runs motor_mqtt_server.py
Listens for MQTT messages and controls motors using motor_controller.py
Joystick Pico W:
Runs joystick_client.py
Reads joystick input and sends movement commands via MQTT

The TC78H653FTG controls both motors using 4 control pins:
IN1, IN2 for Motor A
IN3, IN4 for Motor B
Using PWM on those pins to control the motor speed and direction — which is exactly what you want!
In the class I provided:
PWM on Pin 20/19: Controls Motor 1 (left motor)
PWM on Pin 6/7: Controls Motor 2 (right motor)
Forward:
IN1 = HIGH, IN2 = LOW → Motor A moves forward
IN3 = HIGH, IN4 = LOW → Motor B moves forward
Backward:
IN1 = LOW, IN2 = HIGH → Motor A moves backward
IN3 = LOW, IN4 = HIGH → Motor B moves backward
Turning Left/Right:
By changing the speed or direction of one motor, the robot can turn.
Stop:
Both motors are set to LOW → Stop motion

'''
import network
import time
import math
from machine import Pin, ADC
from umqtt.simple import MQTTClient

# Wi-Fi & MQTT Settings Joystick Client on a pico with Joystick
SSID = "Your_WiFi_SSID"
PASSWORD = "Your_WiFi_Password"
# BROKER = "broker.hivemq.com"
BROKER = 'test.mosquitto.org'
TOPIC = "robot/control"

# Joystick pins
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

dead_zone = 2000

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# Send joystick data via MQTT
def send_command(client, command, speed=50):
    message = f"{command},{speed}"
    client.publish(TOPIC, message)
    print("Sent:", message)

# Main program
def run_joystick():
    client = MQTTClient("joystick_client", BROKER)
    client.connect()
    print("Connected to MQTT broker")

    while True:
        yValue = yAxis.read_u16()
        xValue = xAxis.read_u16()

        if abs(yValue - 50000) < dead_zone and abs(xValue - 50000) < dead_zone:
            send_command(client, "STOP")

        elif yValue < 47500:
            speed = int(((50000 - yValue) / 50000) * 100)
            send_command(client, "FORWARD", speed)

        elif yValue >= 52500:
            speed = int(((yValue - 50000) / 15535) * 100)
            send_command(client, "BACKWARD", speed)

        elif xValue < 47500:
            speed = int(((50000 - xValue) / 50000) * 100)
            send_command(client, "LEFT", speed)

        elif xValue >= 52500:
            speed = int(((xValue - 50000) / 15535) * 100)
            send_command(client, "RIGHT", speed)

        time.sleep(0.1)

# Connect to Wi-Fi and run
connect_wifi()
run_joystick()
