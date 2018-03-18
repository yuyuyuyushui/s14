import shutil, threading, multiprocessing
import time, uuid,os

def copy_file():
    for i in range(100):
        shutil.copyfile(r'C:\Users\Administrator\Desktop\xzrs\111.jpg', r'C:\Users\Administrator\Desktop\xzrs_pic\111'+str(uuid.uuid1())+'.jpg')
def multi_thread():
    streads = []
    for i in range(8):
        t = threading.Thread(target=copy_file(), args=('',))
        streads.append(t)
    for i in streads:
        i.start()
    for i in streads:
        i.join()
if __name__ == '__main__':
    start = time.time()
    multi_threads=[]
    for i in range(4):
        m = multiprocessing.Process(target=multi_thread(),args=('',))
        multi_threads.append(m)
    for i in multi_threads:
        i.start()
    for i in multi_threads:
        i.join()
    print(time.time()-start)