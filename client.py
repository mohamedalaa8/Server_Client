from socket import *
from _thread import *
import threading
def recieve_th (Socket):
    while True :
        z = Socket.recv(2000)
        print("\nServer: ", z.decode('utf-8'))

Socket=socket(AF_INET,SOCK_STREAM)
Socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=7000
Socket.connect((host,port))
recieve=threading.Thread(target=recieve_th,args=(Socket,))
recieve.start()
while 1 :
    Socket.send(input("\nClient: ").encode('utf-8'))
