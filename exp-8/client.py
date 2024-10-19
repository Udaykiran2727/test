import socket

c=socket.socket()

c.connect(('localhost',8888))

n=input("Enter any number:")

c.send(n.encode())

ans=c.recv(1024).decode()
print("Factorial of ",n," is: ",ans)