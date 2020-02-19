'''
SimpleUDPServer.py

A simple demonstration of a UDP server.

author:  Amy Csizmar Dalal
CS 331, Spring 2018
date:  27 April 2018
'''
import socket, sys

class SimpleServer:
    def __init__(self, port=50000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", port))
        
        print ("Listening on port", port)
        
    def listen(self):
        while True:
            try:
                message, address = self.sock.recvfrom(1024)
                msg = message.decode("ascii")
                print ("Received message", msg, "from", address)
                self.sock.sendto(message, address)
                print ("responded")
            except (KeyboardInterrupt, SystemExit) :
                print ("Server interrupted, exiting")
                sys.exit()
            
def main():
    # Create a server
    if len(sys.argv) > 1:
        try:
            server = SimpleServer(int(sys.argv[1]))
        except ValueError:
            print ("Please specify port as an integer.  Creating server on default port.")
            server = SimpleServer()
    else:
        server = SimpleServer()
    
    # Listen forever
    server.listen()

main()