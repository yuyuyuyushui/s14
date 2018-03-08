import threading
import time
def run(n):
    print('task',n)
    time.sleep(3)

t1 = threading.Thread(target=run, args=('new',))#多线程
t2 = threading.Thread(target=run, args=('peace',))

t1.start()
t2.start()
# t1 = run('new')
# t2 = run('peace')

