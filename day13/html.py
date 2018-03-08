import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.bind(('localhost', 8080))

sk.listen()
while 1:
    conn, addr = sk.accept()
    print(conn)

    conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n", "utf8"))
    with open("form表单.html", 'rb') as f:
        file = f.read()
        conn.send(file)

