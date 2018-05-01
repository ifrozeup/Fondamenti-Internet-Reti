from socket import*

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(2) #numero di client in coda

while 1:
    print 'Server pronto'
    connectionSocket, clientAddr = serverSocket.accept()
    
    while 1:
        message = connectionSocket.recv(1024)
        
        if message == '.':
            break
            
        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage)
        
    connectionSocket.close()
