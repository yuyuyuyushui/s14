import multiprocessing
import os,time

def f(i):
    time.sleep(2)
    print(os.getpid())
    return i+200
def bar(arg):
    print('--exce--',arg,os.getpid())
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=5)#建立进程池
    print(os.getpid())
    for i in range(10):
        pool.apply_async(func=f,args=(i,),callback=bar)#并行调用
    print('end')
    pool.close()
    pool.join()