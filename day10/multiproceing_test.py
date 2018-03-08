import multiprocessing
import time,os
def info():#打印进程信息
    print('model_name',__name__)
    print('parent process',os.getppid())
    print('process id',os.getpid())

def run(name):
    info()
    print('%s',name)


if __name__ == '__main__':
    info()#主进程打印

    p = multiprocessing.Process(target=run,args=('bob',))#调用子进程， 子进程的付进程是主进程
    p.start()

