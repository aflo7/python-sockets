#import socket module 
from socket import * 
import sys # In order to terminate the program 
 
# client can run the following to connect to this server: python webclient.py 0.0.0.0 6000 helloWorld.html

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6000
serverSocket.bind(("", serverPort)) #default host: 0.0.0.0
#Fill in end 
serverSocket.listen(1)
print("Listening on port", serverPort)
while True:
    #Establish the connection
    connectionSocket, addr =  serverSocket.accept()         
    try: 
        message = connectionSocket.recv(2048).decode()
        print(message)    
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.read()              
        #Send the content of the requested file to the client
        # at this point, there can be an IOError thrown
            
        headerLine = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(headerLine.encode())
        connectionSocket.send("\r\n".encode())
        
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
         
        connectionSocket.close()
    except IOError: 
        print("Requested file does not exist")
        headerLine = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(headerLine.encode())
        connectionSocket.send("\r\n".encode())