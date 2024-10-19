import socket

c=socket.socket()

c.connect(('localhost',9999))

n=input("Enter a number:")
c.send(n.encode())


response=c.recv(1024).decode()
print(response)


