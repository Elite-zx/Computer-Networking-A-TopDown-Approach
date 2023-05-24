from socket import*
serverPort = 12000 # allocate server port number manually
serverSocket = socket(AF_INET,SOCK_DGRAM)# create server Socket
serverSocket.bind(('',serverPort));# bind socket and port number, one socket one port number
print("The server is ready to receive")
while True:
    message,clientAddress = serverSocket.recvfrom(2048) # receive message from client
    modifiedMessage = message.decode().upper()
    print("done!")
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)

