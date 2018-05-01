from socket import*

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) #ipv4 con TCP
clientSocket.connect((serverName, serverPort))

sentence = raw_input('Input lowercase sentence:')

clientSocket.send(sentence)

modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

clientSocket.close()
