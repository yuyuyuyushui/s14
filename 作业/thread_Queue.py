import queue, shutil, uuid
import threading, time
queue = queue.Queue()
class Thread_copy(threading.Thread):
    def __init__(self, queue):
        super(Thread_copy,self).__init__()
        self.queue = queue
    def run(self):
        while True:
            num = self.queue.get()
            for i in range(num):
                shutil.copyfile(r'C:\Users\Administrator\Desktop\xzrs\111.jpg',
                                r'C:\Users\Administrator\Desktop\xzrs_pic3\111' + str(uuid.uuid1()) + '.jpg')
            self.queue.task_done()
if __name__=='__main__':
    start = time.time()
    for i in range(10):#产生一个thread_pool，开启10个并发
        t = Thread_copy(queue)
        t.setDaemon(True)
        t.start()

    queue.put(10000)
    queue.join()
    print(time.time()-start)