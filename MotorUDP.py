from SolenoidStub import *
import socket, sys


textport = sys.argv[1]
m1 = StubMotor(0)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:
    
    print("Waiting to receive...")
    packet, address = s.recvfrom(port)
    
    if packet:
            print ("Received message from %s: %s" % (address, packet))
            
            if (packet == "Open the Valve"):
                if (m1.status == 0):
                    m1.OpenValve()
                    data = "VALVE OPENED"
                else:
                    data = "VALVE ALREADY OPEN"
                s.sendto(data.encode('utf-8'), address)            
                
            elif (packet == "Close the Valve"):
                if (m1.status == 1):
                    m1.CloseValve()
                    data = "VALVE CLOSED"
                else:
                    data = "VALVE ALREADY CLOSED"
                s.sendto(data.encode('utf-8'), address) 
                
print("Closing...")
s.shutdown(1)