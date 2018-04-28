from socket import*

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('Il server pronto')
cont = 0
while 1:
    connectionSocket, clientAddr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    cont += 1
    print cont
    
