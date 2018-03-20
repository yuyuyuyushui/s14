import multiprocessing, shutil, uuid, time, sys, logging
def func(date_base,num):
    for i in range(num):
        shutil.copyfile(date_base, r'F:\人脸库\曹秀英_511002196310130363'+str(uuid.uuid1())+'.bmp')
if __name__ == '__main__':
    start = time.time()
    multi_list = []
    for i in range(8):
        date_path = r'F:\人脸源\曹秀英_511002196310130363'+str(i)+'.bmp'
        m = multiprocessing.Process(target=func, args=(date_path, 12500))
        m.start()
        multi_list.append(m)
    for i in multi_list:
        i.join()
    print(time.time()-start)
