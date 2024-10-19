import socket

c=socket.socket()

c.connect(('localhost',9999))

filename=input("Enter the name of the file you want to read:")

c.send(filename.encode())

response=c.recv(4096).decode()
print("Server response:")
print(response)