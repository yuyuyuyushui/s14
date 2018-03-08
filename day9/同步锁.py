import threading


def adnum():
    global num
    # r.acquire()#添加锁
    temp = num
    print('ok')
    num = temp - 1
    # r.release()#关闭锁
    # num -= 1


if __name__ == "__main__":
    num = 100
    thread_list = []
    r = threading.Lock()
    for i in range(100):
        t = threading.Thread(target=adnum) # 创建多线程,共享全局变量
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()

    print('num %d' %num)