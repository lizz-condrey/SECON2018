import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """
        
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH) 

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)

           
    def backward(self, speed):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)
        
def slowdown():
    
    motor1.forward(100)
    motor2.forward(100)
    sleep(5)
    motor1.forward(80)
    motor2.forward(80)
    sleep(5)
    motor1.forward(60)
    motor2.forward(60)
    sleep(5)
    motor1.forward(40)
    motor2.forward(40)
    sleep(1)
    motor1.forward(40)
    motor2.forward(40)
    sleep(1)

def turnleft():
        
    motor1.backward(100)
    motor2.backward(100)
    motor3.forward(100)
    motor4.forward(100)
    sleep(2) 
    
def turnright():
    motor1.forward(100)
    motor2.forward(100)
    motor3.backward(100)
    motor4.backward(100)
    sleep(2)
    
        
motor1 = Motor(5, 7, 3)
motor2 = Motor(35, 37, 33)
motor3 = Motor(29, 31, 19)
motor4 = Motor(13, 15, 11)

#motor2 = Motor(13, 15, 11)
#motor3 = Motor(29, 31, 19)
#motor4 = Motor(35, 37, 33)

#motor 1 forward half and full speed
motor1.forward(50)
sleep(3)
motor1.forward(100)
sleep(3)
motor1.stop()
sleep(2)

#motor 2 forward half and full speed
motor2.forward(50)
sleep(3)
motor2.forward(100)
sleep(3)
motor2.stop()
sleep(2)

#motor 3 forward half and full speed
motor3.forward(50)
sleep(3)
motor3.forward(100)
sleep(3)
motor3.stop()
sleep(2)

#motor 4 forward half and full speed
motor4.forward(50)
sleep(3)
motor4.forward(100)
sleep(3)
motor4.stop()
sleep(2)

#motor 1 backward half and full speed
motor1.backward(50)
sleep(3)
motor1.backward(100)
sleep(3)
motor1.stop()
sleep(2)

#motor 2 backward half and full speed
motor2.backward(50)
sleep(3)
motor2.backward(100)
sleep(3)
motor2.stop()
sleep(2)

#motor 3 backward half and full speed
motor3.backward(50)
sleep(3)
motor3.backward(100)
sleep(3)
motor3.stop()
sleep(2)

#motor 4 backward half and full speed
motor4.backward(50)
sleep(3)
motor4.backward(100)
sleep(3)
motor4.stop()
sleep(2)

GPIO.cleanup()
