import socket
import os

def clscr():
    os.system('cls')

host = '127.0.0.1'
port = 8080
obj = socket.socket()
obj.connect((host, port))
message = input('Type message : ')
while message != 'q':
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    if data == 'cls':
        clscr()
    print('Received from server: '+data)
    message = input('type message: ')
obj.close()
