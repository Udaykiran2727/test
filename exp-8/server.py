import socket

s=socket.socket()

s.bind(('localhost',8888))

s.listen(1)

while True:
    c,addr=s.accept()
    print("connected with: ",addr)
    n=c.recv(1024).decode()
    ans=1
    for i in range(2,int(n)+1):
        ans*=i
    c.send(str(ans).encode())
    c.close()