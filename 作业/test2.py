import shutil, uuid,time,threading,queue

def copy_file1():
    for i in range(250):
        shutil.copyfile(r'C:\Users\Administrator\Desktop\xzrs\111.jpg', r'C:\Users\Administrator\Desktop\xzrs_pic\111'+str(uuid.uuid1())+'.jpg')

if __name__=="__main__":
    start = time.time()

    multi_threads1 = []

    for i in range(20):
        m = threading.Thread(target=copy_file1(), args=())
        multi_threads1.append(m)
        m.start()
    for i in multi_threads1:
        i.join()
    print(time.time()-start)
    # print(type(uuid.uuid1()))