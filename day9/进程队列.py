from multiprocessing import Process, Pipe


def f(conn):
    conn.send('nihao')
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()# 类似与socket
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send('hello')
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # prints "[42, None, 'hello']"
#     p.join()