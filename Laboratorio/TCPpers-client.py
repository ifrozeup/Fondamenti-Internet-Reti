from socket import*

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:
    message = raw_input('Inserire messaggio (. per terminare)')
    
    clientSocket.send(message)
    
    if message == '.':
        break
        
    modifiedMessage = clientSocket.recv(1024)
    print 'Message ricevuto: ', modifiedMessage
    
clientSocket.close()
