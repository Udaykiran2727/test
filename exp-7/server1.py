import socket
import os

s=socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(1)
print("waiting for connections")

while True:
    c,addr=s.accept()
    print("Connection established with",addr)
    filename=c.recv(1024).decode()
    
    if os.path.isfile(filename):
        with open(filename,'r') as file:
            data=file.read()
            c.send(data.encode())
    else:
        c.send(bytes("File not found",'utf-8'))
    c.close
    
    