from multiprocessing import Process
import os
import time

def func(name):
    print('start a process')
    time.sleep(3)
    print('the process parent id :', os.getppid())
    print('the process id is :', os.getpid())

if __name__ == '__main__':
    start = time.time()
    processes = []
    for i in range(2):
        p = Process(target=func, args=(i,))
        processes.append(p)
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    print(time.time()-start)