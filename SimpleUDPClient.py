'''
SimpleUDPClient.py

A simple demonstration of a UDP client; sends a message and waits for a reply.

author:  Amy Csizmar Dalal
CS 331, Spring 2018
date:  27 April 2018
'''
import socket, sys, time
from threading import Thread

class SimpleClient:
    def __init__(self, host, port, message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        for i in range(10000):
            msg = (message + " " + str(i)).encode()
            self.sock.sendto(msg, (host, port))
            print ("Sent message", msg.decode(), "to", host, "on port", port)
        
        #msg = message.encode("ascii")
        #self.sock.sendto(msg, (host, port))    
        #print ("Sent message", message, "to", host, "on port", port)
        self.sock.settimeout(8.0)
        
    def processReply(self):
        try:
            while True:
                reply, address = self.sock.recvfrom(4096)
                response = reply.decode("ascii")
                print ("Reply received from", address, ":", response)
        except socket.timeout:
            print ("No reply received, exiting.")
        
def usage():
    print ("Usage:  python SimpleUDPClient <server IP> <port number> <message>")
            
def main():
    # Create a server
    if len(sys.argv) == 4:
        try:
            server = sys.argv[1]
            port = int(sys.argv[2])
            message = sys.argv[3]
        except ValueError:
            usage()
            
    else:
        usage()
        sys.exit()
    
    # Create the client, send the message, and await the reply
    t = Thread(target = client.processReply())
    t.start
    client = SimpleClient(server, port, message)
    #client.processReply()

main()