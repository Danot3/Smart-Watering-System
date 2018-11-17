# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)


valveOpened = False
rainLimit = 55
moistureLimit = 75



while 1:
    print ("\nEnter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break

    s.sendto(data.encode('utf-8'), server_address)
    print("Sent message to %s: %s" % (server_address, data) )
    print("Waiting to receive...")
          
    packet, address = s.recvfrom(port)
            
    if packet:
        print ("Received message from %s: %s" % (address, packet))
        
        if (packet == "Open the Valve"):
            if (not valveOpened):
                valveOpened = True
                data = "VALVE OPENED"
            else:
                data = "VALVE ALREADY OPEN"
            print(data)
            s.sendto(data.encode('utf-8'), server_address)            
                
        elif (packet == "Close the Valve"):
            if (valveOpened):
                valveOpened = False
                data = "VALVE CLOSED"
            else:
                data = "VALVE ALREADY CLOSED"
            print(data)
            s.sendto(data.encode('utf-8'), server_address) 
            
        elif "SetRainLim:" in packet:
            instruct, value = packet.split(":")
            rainLimit = value
            print(rainLimit)
            s.sendto(rainLimit.encode('utf-8'), server_address)
            
        elif "SetMoistureLim:" in packet:
            instruct, value = packet.split(":")
            moistureLimit = value
            print(moistureLimit)
            s.sendto(moistureLimit.encode('utf-8'), server_address)         
        
    else:
        print ("Error: %s" % packet)
    

print("Closing...")
s.shutdown(1)



