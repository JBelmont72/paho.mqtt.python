'''  class to control the motors of your Kitronik Autonomous Robotics Platform using the Toshiba TC78H653FTG motor controller


Toshiba TC78H653FTG Dual H bridge.   This is the data sheet.  https://www.mouser.com/datasheet/2/408/TC78H653FTG_datasheet_en_20190404-1500897.pdf?srsltid=AfmBOooWj2D53FsY5B2hYLJvcabmgjvfAqj0wD7ST0Z58d8D7lZVWMxs.      it appears from the data sheet that these are the pins Pin Functions Pin name IN4/PHA_B IN3/ENB_B NC IN1/ENB_A IN2/PHA_A STBY NC GND OUT2 OUT1 OUT3 OUT4 GND VM LARGE MODE

class to control the motors of your Kitronik Autonomous Robotics Platform using the Toshiba TC78H653FTG motor controller
'''
from machine import Pin, PWM
from time import sleep

class MotorController:
    def __init__(self, motor1_pins, motor2_pins, pwm_freq=1000):
        # Motor 1 pins (Left motor)
        self.motor1_forward = PWM(Pin(motor1_pins['forward']))
        self.motor1_reverse = PWM(Pin(motor1_pins['reverse']))

        # Motor 2 pins (Right motor)
        self.motor2_forward = PWM(Pin(motor2_pins['forward']))
        self.motor2_reverse = PWM(Pin(motor2_pins['reverse']))

        # Set PWM frequency
        self.motor1_forward.freq(pwm_freq)
        self.motor1_reverse.freq(pwm_freq)
        self.motor2_forward.freq(pwm_freq)
        self.motor2_reverse.freq(pwm_freq)

        # Stop motors initially
        self.stop()

    def _set_motor_speed(self, motor_forward, motor_reverse, speed):
        # Cap speed between 0 and 100%
        if speed < 0:
            speed = 0
        elif speed > 100:
            speed = 100

        # Convert speed (0-100%) to PWM value (0-65535)
        pwm_value = int((speed / 100) * 65535)

        motor_forward.duty_u16(pwm_value)
        motor_reverse.duty_u16(0)

    def move_forward(self, speed=50):
        self._set_motor_speed(self.motor1_forward, self.motor1_reverse, speed)
        self._set_motor_speed(self.motor2_forward, self.motor2_reverse, speed)
        print(f"Moving forward at {speed}% speed")

    def move_backward(self, speed=50):
        self._set_motor_speed(self.motor1_reverse, self.motor1_forward, speed)
        self._set_motor_speed(self.motor2_reverse, self.motor2_forward, speed)
        print(f"Moving backward at {speed}% speed")

    def turn_left(self, speed=50):
        self._set_motor_speed(self.motor1_reverse, self.motor1_forward, speed)
        self._set_motor_speed(self.motor2_forward, self.motor2_reverse, speed)
        print(f"Turning left at {speed}% speed")

    def turn_right(self, speed=50):
        self._set_motor_speed(self.motor1_forward, self.motor1_reverse, speed)
        self._set_motor_speed(self.motor2_reverse, self.motor2_forward, speed)
        print(f"Turning right at {speed}% speed")

    def stop(self):
        self.motor1_forward.duty_u16(0)
        self.motor1_reverse.duty_u16(0)
        self.motor2_forward.duty_u16(0)
        self.motor2_reverse.duty_u16(0)
        print("Motors stopped")
