from socket import *
import sys
if len(sys.argv) <= 1: # get listening port
    print('Usage : "python ProxyServer.py listening_port"\n[server_ip : It is the listening\
            port of Proxy Server')
    sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerPort = int(sys.argv[1])
tcpSerSock.bind(('',tcpSerPort))
tcpSerSock.listen(6)
# Fill in end.
while 1:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    # Fill in start.
    message = tcpCliSock.recv(2048).decode()
    # Fill in end.
    print("message content: " , message)
    # Extract the filename from the given message
    print("URL: ", message.split()[1])
    filename = message.split()[1].partition("/")[2].partition("/")[2]
    print("filename: " , filename)
    fileExist = "false"
    # print(filetouse)
    try:# Check wether the file exist in the cache
        f = open(filename, "r")
        outputdata = f.readlines()
        fileExist = "true"
        print("Target file exist!")
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        # send file content
        for i in range(0,len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            print("Target file no exist!")
            # Create a socket on the proxyserver
            # Fill in start.
            c = socket(AF_INET, SOCK_STREAM)
            # Fill in end.
            hostn = message.split()[1].partition("/")[2].partition("/")[0].replace("www.","",1) # remove www. get hostname
            print("source server host: " , hostn )
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn,80))
                print("proxy server's socket connected to source server!")
                # Fill in end.
                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                #print("will open fileobj!")
                #try:
                fileobj = c.makefile('rw',None)
                #except Exception as e:
                #    print("Exception occurred while making file:", str(e))

                print("open fileobj!")
                # approach + url + version of http
                try:
                    number = fileobj.write("GET ".encode()+ filename.encode() + " HTTP/1.0\r\n\r\n".encode())
                    print(number)
                    fileobj.flush()
                except Exception as e:
                    print("Exception occurred while making file:", str(e))
                print("requested sent to source server!")

                # Read the response into buffer
                # Fill in start.
                #c.sendall(message.encode())
                #buff = c.recv(2048)
                buffer = fileobj.read()
                tcpCliSock.sendall(buffer)
                print("buffer is ready!")
                # Fill in end.
                # Create a new file in the cache for the requested file.
                tmpFile = open("./" + filename,"wb")
                # Fill in start.
                tmpFile.write(buffer)
                tmpFile.close()
                # Fill in end.
            except Exception as e:
                print("Exception: ", str(e))
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.1 404 Not Found\r\n\r\n")
            print('File Not Found')
            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end.   
