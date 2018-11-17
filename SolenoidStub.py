#Stub class for Motor. This class allows for testing of the UDP sender/Receiver
#without the solenoid valve

import time

class StubMotor:
    def __init__ (self, status):
        self.status = status
        self.timeOpened = time.time()
        
    #time since valve was opened
    def getTimeSinceOpen(self):
        return time.time()-self.timeOpened

    #opens the valve for the solenoid 
    def OpenValve(self):
        self.status = 1
        print("Valve Opened")
        self.timeOpened = time.time()
        
    
    # Closes the valve for the solenoid 
    def CloseValve(self):
        self.status = 0
        x = str(self.getTimeSinceOpen())
        print("Valve Closed, open for " + x + " seconds")

    #returns the status of the valve
    def getStatus(self):
        return self.status






