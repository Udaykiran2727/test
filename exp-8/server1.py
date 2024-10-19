import socket

s = socket.socket()

s.bind(('localhost', 9999))

s.listen(1)

while True:
    c, addr = s.accept()
    print("Connected with:", addr)

    n = c.recv(1024).decode()
    marks = int(n)

    if marks >= 90 and marks <= 100:
        c.send("Grade S".encode())
    elif marks >= 80 and marks <= 89:
        c.send("Grade A".encode())
    elif marks >= 70 and marks <= 79:
        c.send("Grade B".encode())
    elif marks >= 60 and marks <= 69:
        c.send("Grade C".encode())
    elif marks >= 50 and marks <= 59:
        c.send("Grade D".encode())
    else:
        c.send("Fail".encode())

    c.close()
