import socket
import os

def clscr():
    os.system('cls')

host = '127.0.0.1'
port = 8080
obj = socket.socket()
obj.connect((host, port))
encode = 1024

message = input('Type message : ')
count = 0
while message != 'q':
    count = count + 1
    if (count >= 4):
        clscr()
        count=0
    obj.send(message.encode())
    data = obj.recv(encode).decode()
    print('Received from server: ' + data)
    message = input('type message: ')
obj.close()
