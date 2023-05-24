from socket import*
serverName = '127.0.0.1' # ip or hostname , if is hostname,automatically carry out DNS lookup to find correspond ip
serverPort = 12000 # designate destination port number
clientSocket = socket(AF_INET,SOCK_DGRAM);# create clientsocket, clientPort is automatically allocated by OS
message = input('Input lowercase sentence:')
# message content and destination address(server_ip,server_ port),the clientAddress automatically add to the message by OS     
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048); # receive from server, 2048 is cache length
print(modifiedMessage.decode())
clientSocket.close()
