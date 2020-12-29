##! /usr/bin/python
# a simple tcp server
import socket,os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('192.168.43.245', 12345))  
sock.listen(5)  
while True:  
    connection,address = sock.accept()  
    buf = connection.recv(1024)  
    print (buf)
    connection.send("packet received")    		
connection.close()
