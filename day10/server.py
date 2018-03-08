import socket, time

sk = socket.socket()
sk.bind(('localhost', 8085))
sk.listen(3)
sk.setblocking(False) # 非IO阻塞
while True:
    try:
        conn, addr = sk.accept()#发起系统调用
        print(addr)
        while True:
            date = conn.recv(1024)
            print(date.decode())
            conn.sendall(date.decode().upper().encode('utf-8'))
    except Exception as e:
        print('ok',e)
        time.sleep(3)

    print('ok')