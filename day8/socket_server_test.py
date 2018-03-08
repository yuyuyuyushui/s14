import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                conn = self.request
                while True:
                    date = conn.recv(1024)
                    print(str(date, 'utf-8'))
                    conn.send(date)
                conn.close()
            except OSError:
                break

if __name__=='__main__':
    Host, port = ('localhost', 6088)
    server = socketserver.ThreadingTCPServer((Host, port),MyTCPHandler)
    server.serve_forever()