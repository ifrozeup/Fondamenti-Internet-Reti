from socket import*

serverName = '127.0.0.1'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM) #ipv4 su UDP

clientSocket.settimeout(5)

message = raw_input('Input lowercase sentence:')

try:
    clientSocket.sendto(message, (serverName, serverPort))
    
    response, serverAddress = clientSocket.recvfrom(2048)
    
    print response
except error, v:
    print 'error'
    
    print v
    
clientSocket.close()
