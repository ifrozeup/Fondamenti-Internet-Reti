from socket import*
import time

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

cont = 1

while cont < 100:
    time.sleep(5)
    clientSocket.send('a')
    print 'mando'
    cont += 1

clientSocket.close()
