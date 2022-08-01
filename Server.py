import socket
import os

host = '127.0.0.1'
port = 8080
server = socket.socket()
server.bind((host, port))
server.listen()
conn, addr = server.accept()
print("Connection from: " + str(addr))
encode = 1024


def clscr():
    os.system('cls')
count = 0
while True:
    # Encoding data from client
    count = count + 1
    data = conn.recv(encode).decode()
    if count >= 4:
        clscr()
        count = 0
    if not data:
        break
    print('From connected user: ' + str(data))
    data = str(data)
    print('Message from user : ' + str(data))
    data = input("Type message: ")
    conn.send(data.encode())
