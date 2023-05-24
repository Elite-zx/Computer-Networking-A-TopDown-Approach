from socket import *
import base64
import ssl

msg = "\r\n Elite-ZX love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailServer = 'smtp.gmail.com'
mailPort = 587
fromAddress = 'elite2022zx@gmail.com'
toAddress = '1750802455@qq.com'
username = base64.b64encode(b'elite2022zx@gmail.com').decode()
password = base64.b64encode(b'xmngksvfodayuvwr').decode()
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer,mailPort))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Elite-zx\r\n'
print(heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command and print server response
clientSocket.send(('STARTTLS\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Create TLS connection
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname='smtp.gmail.com')

# Send AUTH LOGIN command 
authLoginCommand='AUTH LOGIN\r\n'
clientSocket.send(authLoginCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')
# Send username
clientSocket.send((username+'\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')
# Send password 
clientSocket.send((password+'\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '235'):
	print('235 reply not received from server')

# Send MAIL FROM command and print server response.
# Fill in start
print('MAIL FROM: <' + fromAddress + '>\r\n')
clientSocket.send(('MAIL FROM: <' + fromAddress + '>\r\n').encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
print('RCPT TO: <'+ toAddress + '>\r\n')
clientSocket.send(('RCPT TO: <'+ toAddress + '>\r\n').encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
DataCommand = 'DATA\r\n'
clientSocket.send(DataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
QuitCommand = 'QUIT\r\n'
clientSocket.send(QuitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
# Fill in end
