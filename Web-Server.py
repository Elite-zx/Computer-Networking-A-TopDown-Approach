#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 80 # allocate server port number manually
serverSocket.bind(('',serverPort))
serverSocket.listen(10) # maximal connection number
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept() ## create a new socket(connectionSocket) which is delicated to client
    #Fill in end
    try:
        #Fill in start
        message = connectionSocket.recv(1024); # receive message from connectionSocket
        #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start
        outputdata = f.read()
        #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        header = 'HTTP/1.1 200 OK\r\nConnection: close\r\nDate: Tue, 23 May 2023 11:14:01 GMT\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' % (len(outputdata))
        connectionSocket.send(header.encode()) 
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode()) 
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end
        serverSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
