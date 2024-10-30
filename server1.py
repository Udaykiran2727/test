import socket
import threading

s=socket.socket()

s.bind(('localhost',9990))

s.listen()

def write(client):
    while True:
        message="client: "+input("")
        try:    
            client.send(message.encode())
        except:
            print("connection closed by server")
            break
def read(client):
    while True:
        try:
            message=client.recv(2048).decode()
            if not message:
                print("client disconnected")
                break
            print(message)
        except:
            print("Connection closed by client.")
            break
while(True):
    c,addr=s.accept()
    print("Connected with {}".format(str(addr)))
    
    thread = threading.Thread(target=write, args=(c,))
    
    thread1 = threading.Thread(target=read, args=(c,))
    
    thread.start()
    thread1.start()
    