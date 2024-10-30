import socket
import threading

c=socket.socket()

c.connect(('localhost',9990))

name=input("Enter your name:")

def write():
    while True:
        try:
            message=name+": "+input("")
            c.send(message.encode())
        except:
            print("connection to server lost!")
            break
        
def read():
    while True:
        try:
            message=c.recv(2048).decode()
            if not message:
                print("Server has closed the connection")
                break
            print(message)
        except ConnectionAbortedError:
            print("Connection closed by server.")
            break
        except ConnectionResetError:
            print("Connection to server lost!")
            break
    c.close()


thread = threading.Thread(target=write)
    
thread1 = threading.Thread(target=read)
    
thread.start()
thread1.start()
    
thread.join()
thread1.join()