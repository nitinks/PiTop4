# This Code displays LED lights RGB depicting the distance of object from Ultrasonic sensor.

# Write your code here :-)
from pitop.pma import LED, Button
from pitop import UltrasonicSensor
from time import sleep

ulSensor = UltrasonicSensor("D3")

class ControlLED:
    def __init__(self):
        self.redLed = LED("D0")
        self.yellowLed = LED("D1")
        self.greenLed = LED("D2")
        
        self.ONLed = None
        
        self.SwitchOff(self.redLed)
        self.SwitchOff(self.yellowLed)
        self.SwitchOff(self.greenLed)
    
    def SwitchOff(self, LED):
        LED.off()
        
    def SwitchOn(self, LED):
        LED.on()
        
    def MakeOn(self, ledName = ""):
        LED = None
        
        if self.ONLed:
            self.SwitchOff(self.ONLed)
            
        if ledName == "red":
            LED = self.redLed
            
        elif ledName == "green":
            LED = self.greenLed
            
        elif ledName == "yellow":
            LED = self.yellowLed
            
        else:
            print("Wrong LED Name")
            
        self.ONLed = LED
        self.SwitchOn(LED)
        
    def MakeOff(self):
        if self.ONLed:
            self.SwitchOff(self.ONLed)
     
cLED = ControlLED()

# Keep reading the distance and turn LED's on.
while True:
    sleep(0.2)
    dist = ulSensor.distance
    
    if(dist < 0.1):
        cLED.MakeOn("red")
    elif (dist > 0.1 and dist < 0.2 ):
        cLED.MakeOn("yellow")
    elif(dist>0.2 and dist <0.4):
        cLED.MakeOn("green")
    else:
        cLED.MakeOff()
        
