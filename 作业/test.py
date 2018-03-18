# import shutil, uuid,time
# def copy_file1():
#     shutil.copyfile(r'C:\Users\Administrator\Desktop\xzrs\111.jpg', r'C:\Users\Administrator\Desktop\xzrs_pic\111'+str(uuid.uuid1())+'.jpg')
#
# if __name__=="__main__":
#     start = time.time()
#     for i in range(10000):
#         copy_file()
#     print(time.time()-start)
    # print(type(uuid.uuid1()))
import shutil, uuid, time, queue, gevent


def copy_file(data_base, num):
    for i in range(num):
        shutil.copyfile(data_base, r'C:\Users\Administrator\Desktop\xzrs_pic1\111' + str(uuid.uuid1()) + '.jpg')


if __name__ == "__main__":
    start = time.time()
    gevent.joinall([gevent.spawn(copy_file, r'C:\Users\Administrator\Desktop\xzrs\111.jpg', 2500),
                    gevent.spawn(copy_file, r'C:\Users\Administrator\Desktop\xzrs\112.jpg', 2500),
                    gevent.spawn(copy_file, r'C:\Users\Administrator\Desktop\xzrs\113.jpg', 2500),
                    gevent.spawn(copy_file, r'C:\Users\Administrator\Desktop\xzrs\114.jpg', 2500),
                    ])
    print(time.time() - start)