import shutil, multiprocessing, queue
import time, uuid
q = queue.Queue()

def copy_file(data_base):
    for i in range(25000):
        shutil.copyfile(data_base, r'C:\Users\Administrator\Desktop\xzrs_pic2\111'+str(uuid.uuid1())+'.jpg')

if __name__=='__main__':
    start = time.time()
    multi_threads = []
    for i in range(4):
        m = multiprocessing.Process(target=copy_file, args=(r'C:\Users\Administrator\Desktop\xzrs\11'+str(i+1)+'.jpg',))
        multi_threads.append(m)
        m.start()
    # m1 = multiprocessing.Process(target=copy_file, args=(r'C:\Users\Administrator\Desktop\xzrs\111.jpg',))
    # m2 = multiprocessing.Process(target=copy_file, args=(r'C:\Users\Administrator\Desktop\xzrs\112.jpg',))
    # m3 = multiprocessing.Process(target=copy_file, args=(r'C:\Users\Administrator\Desktop\xzrs\113.jpg',))
    # m4 = multiprocessing.Process(target=copy_file, args=(r'C:\Users\Administrator\Desktop\xzrs\114.jpg',))
    # multi_threads.append(m1)
    # multi_threads.append(m2)
    # multi_threads.append(m3)
    # multi_threads.append(m4)
    # for i in multi_threads:
    #     i.start()
    for i in multi_threads:
        i.join()
    print(time.time() - start)