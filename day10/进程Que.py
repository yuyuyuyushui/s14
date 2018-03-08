import multiprocessing
def f(qq):#子进程和父进程交换数据
    qq.put(['luo','qiang'])
if __name__ == '__main__':
    q = multiprocessing.Queue()#建立传递数据对象
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()