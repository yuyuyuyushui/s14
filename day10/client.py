import socket
client = socket.socket()
client.connect(('localhost',8085))

while True:

    client.sendall('hello'.encode('utf-8'))
    date = client.recv(1024)
    print(date.decode())
