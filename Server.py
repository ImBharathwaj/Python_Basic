import socket

host = "127.0.0.1"
port = 5001
# Creating a socket
server = socket.socket()
# Binding network attributes with it
server.bind((host,port))
# Make it listen
server.listen()

# Bringing connection and address of the client network
conn, addr = server.accept()

print('Connection from: '+str(addr))
while True:

    # Receiving data from collection
    data = conn.recv(2048).decode()
    if not data:
        break
    print('from connection user : '+str(data))

    data = str(data).upper()
    print('Received from user : '+str(data))
    data = input('Type message : ')
    conn.send(data.encode())

conn.close()