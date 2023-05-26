from socket import*
serverName = '127.0.0.1'
serverPort = 12000   # welcoming socket
clientSocket = socket(AF_INET, SOCK_STREAM)#clientPort is automatically allocated by OS
# knock at the welcoming door(welcomingsocket),this will initiate tcp three-way handshakes
clientSocket.connect((serverName,serverPort)) 
sentence=input('Input lowercase sentence:')
clientSocket.send(sentence.encode()) # send message without server addree,since tcp connection is built
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()

