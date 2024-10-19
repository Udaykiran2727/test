import socket

s=socket.socket()

print("socket created")

s.bind(('localhost',9999))

s.listen(1)

print("waiting for connections")

while True:
    c,addr=s.accept()
    n=c.recv(1024).decode()
    print("connected with:",addr)
    try:
        n=int(n)
        response = '\n'.join('*' * (n - i) for i in range(n))
    except ValueError:
        response="Invalid input"
        
    c.send(response.encode())
    c.close()