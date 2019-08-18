from gpiozero import Servo
from time import sleep
 
myGPIO=18
 
servo = Servo(myGPIO)
 
while True:
    servo.mid()
    print("Mid")
    sleep(0.5)
    servo.min()
    print("Min")
    sleep(1)
    servo.mid()
    print("Mid")
    sleep(0.5)
    servo.max()
    print("Max")
    sleep(1)
