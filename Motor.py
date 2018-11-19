#import RPi.GPIO as GPIO
import time

class Motor:
    def __init__ (self, status):
        self.status = status
        self.timeOpened = time.time()
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(11,GPIO.OUT)
        
    #time since valve was opened
    def getTimeSinceOpen(self):
        return time.time()-self.timeOpened

    #opens the valve for the solenoid 
    def OpenValve(self):
        #GPIO.output(11,GPIO.HIGH)
        self.status = 1
        print("Valve Opened")
        self.timeOpened = time.time()
        
    
    # Closes the valve for the solenoid 
    def CloseValve(self):
        #GPIO.output(11,GPIO.LOW)
        self.status = 0
        x = str(self.getTimeSinceOpen())
        print("Valve Closed, open for " + x + " seconds")

    #returns the status of the valve
    def getStatus(self):
        return self.status
    
#m1 = Motor(0)
#m1.OpenValve()
#time.sleep(2)
#m1.CloseValve()