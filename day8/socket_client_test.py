import socket

client = socket.socket()

client.connect(('localhost', 6088))

while True:
    ssh_mess = input('请输入对象>>').strip()
    client.send(bytes(ssh_mess, 'utf-8'))
    date = client.recv(1024)
    print(str(date, 'utf-8'))
    client.close()