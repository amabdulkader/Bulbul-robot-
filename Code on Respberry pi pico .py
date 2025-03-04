from machine import Pin,PWM #importing PIN and PWM
import time #importing time
import utime
from machine import UART
from machine import Pin
led=Pin(25,Pin.OUT)
uart=UART(0,9600)
# Defining motor pins
motor1=Pin(15,Pin.OUT)
motor2=Pin(11,Pin.OUT)
motor3=Pin(12,Pin.OUT)
motor4=Pin(13,Pin.OUT)
# m2=Pin(15,Pin.OUT)
# Defining enable pins and PWM object
enable1=PWM(Pin(6))
enable2=PWM(Pin(7))

# Defining  right and left IR digital pins as input
right_ir = Pin(2, Pin.IN)
left_ir = Pin(3, Pin.IN)


# Defining frequency for enable pins
# enable1.freq(1000)
# enable2.freq(1000)

# Setting maximum duty cycle for maximum speed
# enable1.duty_u16(65025)
# enable2.duty_u16(65025)

# Forward
def move_forward():
    motor1.low()
    motor2.high()
    motor3.high()
    motor4.low()
    pass
# Backward
def move_backward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high()
#     pass  
#Turn Right
def turn_right():
    motor1.high()
    motor2.high()
    motor3.low()
    motor4.low()    
#Turn Left
def turn_left():
    motor1.low()
    motor2.low()
    motor3.high()
    motor4.high()
   
#Stop
def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()
def auto():
    while True:
        right_val=right_ir.value() #Getting right IR value(0 or 1)
        left_val=left_ir.value() #Getting left IR value(0 or 1)
        
        print(str(right_val)+"-"+str(left_val))
        if right_val==0 and left_val==0:
            motor1.low()
            motor2.high()
            motor3.high()
            motor4.low()
#                 pass
        elif right_val==1 and left_val==0:
            motor1.low()
            motor2.low()
            motor3.high()
            motor4.high()
        elif right_val==0 and left_val==1:
            motor1.high()
            motor2.high()
            motor3.low()
            motor4.low()    

        else:
            motor1.low()
            motor2.low()
            motor3.low()
            motor4.low()
            break
def returnline():
    while True:
        right_val=right_ir.value() #Getting right IR value(0 or 1)
        left_val=left_ir.value() #Getting left IR value(0 or 1)
        
        print(str(right_val)+"-"+str(left_val))
        
        if right_val==1 and left_val==1:
            motor1.high()
            motor2.high()
            motor3.low()
            motor4.low()    
        elif right_val==1 and left_val==0:
            motor1.high()
            motor2.high()
            motor3.low()
            motor4.low() 
        elif right_val==0 and left_val==0:
            motor1.high()
            motor2.high()
            motor3.low()
            motor4.low() 
        elif right_val==0 and left_val==1:
            motor1.low()
            motor2.low()
            motor3.low()
            motor4.low()
            break
            
while True:
    right_val=right_ir.value() #Getting right IR value(0 or 1)
    left_val=left_ir.value() #Getting left IR value(0 or 1)
#     print(str(right_val)+"-"+str(left_val))

    
    if uart.any()>0:
            message=uart.readline()
            if message is not None:
                message = message.decode("utf-8")
                print(message)
                if message == 'B' :
                    move_backward()
                if message == 'F' :
                    move_forward()
                    
                if message == 'L' :
                    turn_left()
                if message == 'R' :
                    turn_right()
                    
                if message == 'H' :
                    led.value(1)
                    auto()
                if message == 'J' :
                    led.value(1)
                    returnline()
                if message =='S':
                    stop()
    
    # Controlling robot direction based on IR value
        
    
    
    

# motor1.high()
# motor2.low()
# motor3.low()
# motor4.high()



# motor1.low()
# motor2.low()
# motor3.high()
# motor4.high()


# motor1.high()
# motor2.high()
# motor3.low()
# motor4.low()

# motor1.high()
# motor2.low()
# motor3.low()
# motor4.high()

# motor1.low()
# motor2.high()
# motor3.high()
# motor4.low()


# motor1.low()
# motor2.low()
# motor3.low()
# motor4.low()
