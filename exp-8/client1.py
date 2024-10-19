import socket

c=socket.socket()

c.connect(('localhost',9999))

n=input("Enter your marks")

c.send(n.encode())

print(c.recv(1024).decode())