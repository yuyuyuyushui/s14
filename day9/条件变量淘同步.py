import threading, time


from random import randint

class Producer(threading.Thread):#生产者
    def run(self):
        global L
        while True:
            var = randint(1, 100)
            print('生产者', self.name, ":append"+str(var),  L)
            if lock_acqui.acquire(): # 加锁
                L.append(var)
                lock_acqui.notify()
                lock_acqui.release()
            time.sleep(3)

class Consumer(threading.Thread):#消费者
    def run(self):
        global L
        while True:
            lock_acqui.acquire()
            if len(L) == 0:
                lock_acqui.wait() #多线程之间的通信
            print('消费者', self.name, ':del'+str(L[0]), L)
            del L[0]
            lock_acqui.release()
            time.sleep(0.25)



if __name__ =='__main__':
    L = []
    lock_acqui = threading.Condition()
    threas = []
    for i in range(5):
        threas.append(Producer())
    threas.append(Consumer())# 5+1个线程开启
    for t in threas:
        t.start()
    for t in threas:
        t.join()
