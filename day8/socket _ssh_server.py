import socket
import os

server = socket.socket()
Host = 'localhost'
Port = 6866
Buffsize = 1024
Addr = (Host, Port)

server.bind(Addr)
server.listen()#设置并启动TCP监听

while True:

    print('waiting for connection ...')
    conn, addr = server.accept()
    while True:
        date = conn.recv(Buffsize)
        print(type(date))
        if not date:
            break
        print(type(date.decode()))
        cms_res = os.popen(date.decode()).read()
        print(type(cms_res))
        conn.send(str(len(cms_res.encode())).encode())
        conn.send(cms_res.encode('utf-8'))
      #  print(date)

server.close()