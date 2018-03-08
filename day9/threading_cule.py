import threading
import time

def run(n):
    print('tast',n)
    time.sleep(2)
    print('task done')

star_time = time.time()
t_obje = []

for i in range(50):
    t = threading.Thread(target=run, args=(i,))
    t.setDaemon(True)#设置守护进程
    t.start()
    t_obje.append(t)#存储每一个线程的对象
# for t in t_obje:
#     t.join()#主线程等所有线程执行完

print('-------task  done!=-----------')
print('cost %s', time.time() - star_time)
