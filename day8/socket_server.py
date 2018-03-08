import socket, subprocess, os

server = socket.socket()

server.bind(('localhost', 8085))
server.listen()#设置并启动TCP监听

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = server.accept()
    while True:
        try:
            date = conn.recv(1024)
        except Exception:
            break
        if not date: break

        cmd, filename, file_size = date.decode('utf-8').split('|')
        path = os.path.join(BASE_DIR,'test', filename)
        date_file = 0
        with open(path, 'wb') as f:
            while int(file_size) != date_file:
                date = conn.recv(1024)
                f.write(date)
                date_file += len(date)
        conn.send('上传成功'.encode('utf-8'))
    server.close()