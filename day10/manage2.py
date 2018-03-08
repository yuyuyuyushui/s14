import multiprocessing
import os


def f(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())

if __name__ == '__main__':
    with multiprocessing.Manager() as manage:#等于manage = multiprocessing.Manager()格式化一个传递信息，自带锁
        d = manage.dict()
        l = manage.list(range(5))
        p_list = []
        for i in range(10):
            p = multiprocessing.Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:#等待结果
            res.join()
        print(d)
        print(l)