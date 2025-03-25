'''L293N motor driver
https://www.youtube.com/watch?v=H1Fzil_VUq4&t=159s
https://github.com/Guitarman9119/Raspberry-Pi-Pico-/blob/main/L298N%20motor%20driver%20module/example2.py
many tutorials- Guitarman       https://github.com/Guitarman9119/Raspberry-Pi-Pico-/tree/main
'''
# from machine import Pin
# import time #importing time for delay  

# # Defining motor pins

# #OUT1  and OUT2
# In1=Pin(0,Pin.OUT) 
# In2=Pin(1,Pin.OUT)  
# EN_A=Pin(4,Pin.OUT)

# #OUT3  and OUT4
# In3=Pin(2,Pin.OUT)  
# In4=Pin(3,Pin.OUT)  
# EN_B=Pin(5,Pin.OUT)

# EN_A.high()
# EN_B.high()
# # Forward
# def move_forward():
#     In1.high()
#     In2.low()
#     In3.high()
#     In4.low()
    
# # Backward
# def move_backward():
#     In1.low()
#     In2.high()
#     In3.low()
#     In4.high()
    
# #Turn Right
# def turn_right():
#     In1.low()
#     In2.low()
#     In3.low()
#     In4.high()
    
# #Turn Left
# def turn_left():
#     In1.low()
#     In2.high()
#     In3.low()
#     In4.low()
   
# #Stop
# def stop():
#     In1.low()
#     In2.low()
#     In3.low()
#     In4.low()
    
# while True:
#     move_forward()
#     print("Forward")
#     time.sleep(2)
#     stop()
#     print("Stop")
#     time.sleep(2)
#     move_backward()
#     print("Backward")   
#     time.sleep(2)
#     stop()
#     print("Stop")
#     time.sleep(2)
 ###~~~~~~ second motor program with PWM control 
'''  
import sys  
from machine import Pin, ADC, PWM  #importing PIN,ADC and PWM
import time #importing time   
import utime 
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
# Defining motor pins

#OUT1  and OUT2
In1=Pin(0,Pin.OUT) 
In2=Pin(1,Pin.OUT)  
EN_A=PWM(Pin(4))


#OUT3  and OUT4
In3=Pin(2,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=PWM(Pin(5))


# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)


# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()


while True:
    time.sleep(0.5)
    
    yValue = yAxis.read_u16()
    xValue = xAxis.read_u16()
    print('yValue: ',yValue)
    print('xValue: ',xValue)
    
    # if yValue >= 32000 and yValue <= 34000 or xValue >= 32000 and xValue <= 34000:

    #     stop()
        

    
    
    if yValue >= 52500:
        duty_cycle=(100/15535)*yValue- 321.87
        # duty_cycle = (((yValue-65535/2)/65535)*100)*2
        print("Move backward: Speed " + str(duty_cycle) + " %")
        # duty_cycle = ((yValue/65535)*100)*650.2
        # duty_cycle=yValue
        EN_A.duty_u16(int(duty_cycle))
        EN_B.duty_u16(int(duty_cycle))
        
        move_backward()

        

    
    elif yValue < 47500:
        duty_cycle=-1.316*yValue +65800
        # duty_cycle = ((yValue-65535/2)/65535*100)*2
        print("Move Forward: Speed " + str(abs(duty_cycle)) + " %")
        # duty_cycle = abs(duty_cycle)*650.2
        # duty_cycle=yValue
        EN_A.duty_u16(int(duty_cycle))
        EN_B.duty_u16(int(duty_cycle))
        
        move_forward()
 '''      
       
    # elif xValue < 32000:
    #     duty_cycle = (((xValue-65535)/65535)*100)
    #     print("Move Left: Speed " + str(abs(duty_cycle)) + " %")
    #     duty_cycle = abs((duty_cycle)*650.25)

    #     EN_B.duty_u16(0)
    #     EN_A.duty_u16(int(duty_cycle))
        
    #     move_forward()


    # elif xValue > 34000:
    #     duty_cycle = ((xValue-65535/2)/65535*100)*2
    #     print("Move Right: Speed " + str(abs(duty_cycle)) + " %")
    #     duty_cycle = abs(duty_cycle)*650.2

    #     EN_B.duty_u16(int(duty_cycle))
    #     EN_A.duty_u16(0)
        
    #     move_forward()
    
    

        
    
    
    



'''
try:
    while True:
        time.sleep(0.5)
        
        yValue = yAxis.read_u16()
        xValue = xAxis.read_u16()
        print(f'Y_value: {yValue}')
        print(f'X_value: {xValue}')
        if yValue <50000:
            forward_percent = abs(.002*yValue -100)
            print(forward_percent)
            print("Move Forward: Speed " + str(forward_percent) + " %")

            EN_A.duty_u16(int(forward_percent))
            EN_B.duty_u16(int(forward_percent))
            # duty_cycle = abs(duty_cycle)*650.2

            # EN_A.duty_u16(int(duty_cycle))
            # EN_B.duty_u16(int(duty_cycle))
            
            move_forward()
  
    #     if yValue >= 32000 and yValue <= 34000 or xValue >= 32000 and xValue <= 34000:

    #         stop()
            

        
        
    #     if yValue >= 34000:
    #         duty_cycle = (((yValue-65535/2)/65535)*100)*2
    #         print("Move backward: Speed " + str(abs(duty_cycle)) + " %")
    #         duty_cycle = ((yValue/65535)*100)*650.2
            
    #         EN_A.duty_u16(int(duty_cycle))
    #         EN_B.duty_u16(int(duty_cycle))
            
    #         move_backward()

            

        
    #     elif yValue <= 32000:
    #         duty_cycle = ((yValue-65535/2)/65535*100)*2
    #         print("Move Forward: Speed " + str(abs(duty_cycle)) + " %")
    #         duty_cycle = abs(duty_cycle)*650.2

    #         EN_A.duty_u16(int(duty_cycle))
    #         EN_B.duty_u16(int(duty_cycle))
            
    #         move_forward()
        
        
    #     elif xValue < 32000:
    #         duty_cycle = (((xValue-65535)/65535)*100)
    #         print("Move Left: Speed " + str(abs(duty_cycle)) + " %")
    #         duty_cycle = abs((duty_cycle)*650.25)

    #         EN_B.duty_u16(0)
    #         EN_A.duty_u16(int(duty_cycle))
            
    #         move_forward()


    #     elif xValue > 34000:
    #         duty_cycle = ((xValue-65535/2)/65535*100)*2
    #         print("Move Right: Speed " + str(abs(duty_cycle)) + " %")
    #         duty_cycle = abs(duty_cycle)*650.2

    #         EN_B.duty_u16(int(duty_cycle))
    #         EN_A.duty_u16(0)
            
    #         move_forward()
        
except KeyboardInterrupt:
    sys.exit()       
'''
            
        
        
    
# import sys  
# from machine import Pin, ADC, PWM  
# import time  

# xAxis = ADC(Pin(27))
# yAxis = ADC(Pin(26))

# # Motor pins
# In1 = Pin(0, Pin.OUT)
# In2 = Pin(1, Pin.OUT)
# In3 = Pin(2, Pin.OUT)
# In4 = Pin(3, Pin.OUT)

# EN_A = PWM(Pin(4))
# EN_B = PWM(Pin(5))

# # Set PWM frequency
# EN_A.freq(1500)
# EN_B.freq(1500)

# dead_zone = 2000

# # Motor functions
# def move_forward():
#     In1.high()
#     In2.low()
#     In3.low()
#     In4.high()

# def move_backward():
#     In1.low()
#     In2.high()
#     In3.high()
#     In4.low()

# def stop():
#     In1.low()
#     In2.low()
#     In3.low()
#     In4.low()

# while True:
#     time.sleep(0.1)

#     yValue = yAxis.read_u16()
#     xValue = xAxis.read_u16()
#     print('yValue: ', yValue)
#     print('xValue: ', xValue)

#     if abs(yValue - 50000) < dead_zone:
#         stop()
#         print("Joystick in dead zone — motors stopped.")
    
#     elif yValue < 47500:
#         duty_cycle = int((-1.316 * yValue) + 65800)
#         duty_cycle = min(max(duty_cycle, 0), 65535)
#         print("Move Forward: Speed " + str(duty_cycle))
        
#         EN_A.duty_u16(duty_cycle)
#         EN_B.duty_u16(duty_cycle)
#         move_forward()

#     elif yValue >= 52500:
#         duty_cycle = int((yValue - 50000) * (65535 / 15535))
#         duty_cycle = min(max(duty_cycle, 0), 65535)
#         print("Move Backward: Speed " + str(duty_cycle))
        
#         EN_A.duty_u16(duty_cycle)
#         EN_B.duty_u16(duty_cycle)
#         move_backward()



import sys  
from machine import Pin, ADC, PWM  
import time  
import math  

xAxis = ADC(Pin(27))  
yAxis = ADC(Pin(26))  

# Motor pins  
In1 = Pin(0, Pin.OUT)  
In2 = Pin(1, Pin.OUT)  
In3 = Pin(2, Pin.OUT)  
In4 = Pin(3, Pin.OUT)  

EN_A = PWM(Pin(4))  
EN_B = PWM(Pin(5))  

# Set PWM frequency  
EN_A.freq(1500)  
EN_B.freq(1500)  

dead_zone = 2000  

# Motor functions  
def move_forward():  
    In1.high()  
    In2.low()  
    In3.low()  
    In4.high()  

def move_backward():  
    In1.low()  
    In2.high()  
    In3.high()  
    In4.low()  
def move_left():  
    In1.high()  
    In2.low()  
    In3.high()  
    In4.low()  

def move_right():  
    In1.high()  
    In2.low()  
    In3.high()  
    In4.low()  

def stop():  
    In1.low()  
    In2.low()  
    In3.low()  
    In4.low()  

# Logarithmic scaling function the max_input for the forward is 50000 for backward is 65535
def scale_speed(value, min_input, max_input, min_output, max_output):  
    if value <= min_input:  
        return min_output  
    scaled_value = math.log(value - min_input + 1) / math.log(max_input - min_input + 1)  
    return int(min_output + (scaled_value * (max_output - min_output)))

while True:  
    time.sleep(0.1)  

    yValue = yAxis.read_u16()  
    xValue = xAxis.read_u16()  
    print('yValue: ', yValue)  
    print('xValue: ', xValue)  

    # if abs(yValue - 50000)  < dead_zone:  
    if abs(yValue - 50000) and abs(xValue-50000)  < dead_zone:  
        stop()  
        print("Joystick in dead zone — motors stopped.")  

    elif yValue < 47500: ## the 50000-yValue  increases as the joystick is pushed up, when gets to 65535 is max speed
                          ##scale_speed(value, min_input, max_input, min_output, max_output)
        scaled_speed = scale_speed(50000 - yValue, 0, 50000, 1000, 65535)  
        print("Move Forward: Speed " + str(scaled_speed))  
        
        EN_A.duty_u16(scaled_speed)  
        EN_B.duty_u16(scaled_speed)  
        move_forward()  

    elif yValue >= 52500:
                      ##scale_speed(value, min_input, max_input, min_output, max_output)
        scaled_speed = scale_speed(yValue, 50000, 65535, 1000, 65535)  
        print("Move Backward: Speed " + str(scaled_speed))  
        
        EN_A.duty_u16(scaled_speed)  
        EN_B.duty_u16(scaled_speed)  
        move_backward()
    elif xValue < 47500: ## the 50000-yValue  increases as the joystick is pushed up, when gets to 65535 is max speed
                          ##scale_speed(value, min_input, max_input, min_output, max_output)
        scaled_speed = scale_speed(50000 - xValue, 0, 50000, 1000, 65535)  
        print("Move Left: Speed " + str(scaled_speed))  
        
        EN_A.duty_u16(scaled_speed)  
        EN_B.duty_u16(scaled_speed)  
        move_left()  

    elif xValue >= 52500:
                      ##scale_speed(value, min_input, max_input, min_output, max_output)
        scaled_speed = scale_speed(xValue, 50000, 65535, 1000, 65535)  
        print("Move Right: Speed " + str(scaled_speed))  
        
        EN_A.duty_u16(scaled_speed)  
        EN_B.duty_u16(scaled_speed)  
        move_right()
########~~~~~~~~~~~~~~~~log practice
# import math
# def scale_speed(value, min_input, max_input, min_output, max_output):  
#     if value <= min_input:  
#         return min_output  
#     scaled_value = math.log(value - min_input + 1) / math.log(max_input - min_input + 1)
#     Numerator=math.log(value - min_input + 1)
#     Denominator= math.log(max_input - min_input + 1)
#     print(Numerator,'  ',Denominator)   ## output 9.650915    9.650915
#     print(f'scaled_value:  {scaled_value} :  {scaled_value*(max_input-min_output)}')  
#     return int(min_output + (scaled_value * (max_output - min_output)))## subtracts the min output from multiplyiny the scalled value but adds it back in 

# yValue=60000
# if yValue >=50000:
#     scaled_speed = scale_speed(yValue, 50000, 65535, 1000, 65535)
# print(scaled_speed)

# Num=math.log(50001 - 50000 + 1) ## natural logs output 0.6931472 for 2
# print(Num)
# # Python code to demonstrate the working of
# # log(a,Base)
# ##ln4=1.386 ln5=1.6094  ln4/ln5=.86119  5 to the .8619 power =4  !!!
# import math

# # Printing the log base e of 14
# print ("Natural logarithm of 14 is : ", end="")
# print (math.log(14))

# # Printing the log base 5 of 14
# print ("Logarithm base 5 of 14 is : ", end="")
# print (math.log(14,5))
