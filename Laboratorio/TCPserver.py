from socket import*

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) # prepara alla connessione

serverSocket.listen(1) #passive open, accetta solo una connessione in coda 
print ('The server is ready to receive')

while 1:
    connectionSocket, clientAddr = serverSocket.accept()
    
    message = connectionSocket.recv(1024)
    
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage)
    
    connectionSocket.close()
