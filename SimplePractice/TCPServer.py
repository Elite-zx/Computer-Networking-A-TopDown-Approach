from socket import*
serverPort = 12000 # welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1) # maximal connection number(at least 1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept() # create a new socket(connectionSocket) which is delicated to client
    sentence = connectionSocket.recv(1024).decode() # receive message from connectionSocket
    capitalizedSentence = sentence.upper()
    print("done!")
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
