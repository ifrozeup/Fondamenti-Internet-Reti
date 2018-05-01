from socket import*
import thread

def handler(newSocket):
    while 1:
        message = newSocket.recv(1024)
        if message == '.':
            break
        modifiedMessage = message.upper()
        newSocket.send(modifiedMessage)
    newSocket.close() 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

#opzione per riciclare la porta
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while 1:
    print 'Server pronto'
    connectionSocket, clientAddr = serverSocket.accept()
    thread.start_new_thread(handler, (connectionSocket, ))
