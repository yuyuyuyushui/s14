from multiprocessing import Process, Queue

def f(q):
    q.put([42,2,'hello'])
    print('subprocess id:', id(q))

if __name__=='__main__':
    q = Queue()
    p_list = []
    print('main q id:', id(q))

    for i in range(3):
        t = Process(target=f, args=(q,))
        t.start()
        p_list.append(t)

    print(q.get())
    print(q.get())
    print(q.get())
    for t in p_list:
        t.join()
