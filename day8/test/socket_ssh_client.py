import  socket

client = socket.socket()
Host = 'localhost'
Port = 8080
Buffsize = 1024
Addr = (Host, Port)

client.connect(Addr)

while True:
    pos = input('>>:').strip()
    client.send(pos.encode('utf-8'))
    date_sizes = client.recv(Buffsize)#返回是二进制
    date_size = 0
    date2 = b''
    while date_size < int(date_sizes.decode()):
        date = client.recv(Buffsize)
        date_size += len(date)
        date2 += date
        print(type(date_sizes))
        print(date_sizes.decode())
    else:
        print(date2.decode())
    client.close()