from socket import*
import time 

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM);
clientSocket.settimeout(1)  # timeout is 1 second 

for i in range(0,10):
    sendTime = time.time() 
    message =('Ping %d %s' % (i+1,sendTime)).encode()
    try:
        clientSocket.sendto(message,(serverName,serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        rtt = time.time() - sendTime
        print('Sequence %d: RTT = %.3fs  Reply from %s' % (i+1,rtt,serverName))
    except Exception: # time out Exception, socket.timeout is not from BaseException
        print('Sequence %d: Request timed out' % (i+1))

clientSocket.close()

