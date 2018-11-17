import socket, sys, time

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)


def sendAck(packet, address):
    message = "ACK: " + packet
    s.sendto(message, address)   
    print ("Sent acknowledgement to %s: %s" % (address, message)) 
    

def sendCloseValveInstruction(address):
    instruction = "Close the Valve"
    s.sendto(instruction, address)
    print ("Sent instruction to %s: %s" % (address, instruction)) 
    packet, address = s.recvfrom(port)
    print(packet)


def sendOpenValveInstruction(address):
    instruction = "Open the Valve"
    s.sendto(instruction, address)
    print ("Sent instruction to %s: %s" % (address, instruction)) 
    packet, address = s.recvfrom(port)
    print(packet)
    

def sendSetRainLimInstruct(packet, address):
    s.sendto(packet, address)
    print ("Sent instruction to %s: %s" % (address, packet)) 
    packet, address = s.recvfrom(port)
    print(packet)
    
    
def sendSetMoistureLimInstruct(packet, address):
    s.sendto(packet, address)
    print ("Sent instruction to %s: %s" % (address, packet)) 
    packet, address = s.recvfrom(port)
    print(packet) 


while True:

    print ("\nWaiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop\n" % port)

    packet, address = s.recvfrom(port)
    
    print ("Received %s bytes from %s: %s" % (len(packet), address, packet))
    
    if packet == "MoistureLimPassed":
        sendCloseValveInstruction(address)
        
    elif packet == "RainLimPassed":
        sendCloseValveInstruction(address)
        
    elif packet == "Testing":
        sendAck(packet, address)      
    
    elif packet == "ManualOpen":
        sendOpenValveInstruction(address)
        
    elif packet == "ManualClose":
        sendCloseValveInstruction(address)

    elif "SetRainLim:" in packet:
        sendSetRainLimInstruct(packet, address) 
        
    elif "SetMoistureLim:" in packet:
        sendSetMoistureLimInstruct(packet, address)     
        
    else:
        s.sendto("PACKET ERROR", address)
        print ("Valid instruction required.")
        
        
print("Closing...")
s.shutdown(1)

