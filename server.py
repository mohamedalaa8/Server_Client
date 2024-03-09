from socket import *
from _thread import *
import threading
def recieve_th (secion_number):
    while True :
        A = secion_number.recv(2000)
        print("\nClient: ", A.decode('utf-8'))
def client_th (secion_number):
    recieve = threading.Thread(target=recieve_th,args=(secion_number,))
    recieve.start()
    while 1 :
        secion_number.send(input("\nServer: ").encode('utf-8'))

Socket=socket(AF_INET,SOCK_STREAM)
Socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=7000
Socket.bind((host,port))
Socket.listen(5)
print("Wait")
try:
    while 1 :
        secion_number,address=Socket.accept()
        print("sucessfuly",address[0])
        start_new_thread(client_th,(secion_number,))
except:
    print("finished")
    Socket.close()