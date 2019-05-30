from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print ('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print ('connect from: ', addr)
    
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        send = bytes(ctime(),'utf-8')+data
        tcpCliSock.send(send)
        
    tcpCliSock.close()
tcpSerSock.close()
