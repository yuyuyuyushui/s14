import socket, subprocess, os

client = socket.socket()

client.connect(('localhost', 8085))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    ssh_mess = input('请输入对象>>').strip()
    if ssh_mess == 'e':
        break
    cmd, path =ssh_mess.split('|')
    path = os.path.join(BASE_DIR, path)
    filename = os.path.basename(path) # 获取文件的名字
    filesize = os.stat(path).st_size # 获取文件的大小
    file_info = 'post|%s|%s'%(filename, filesize)
    print(file_info)
    client.send(file_info.encode('utf-8'))
    with open(path, 'rb') as f:
        file_date = 0
        while file_date != filesize:
            file_pic = f.read(1024)
            client.send(file_pic)
            file_date += len(file_pic)
    date = client.recv(1024)
    print(date.decode())
client.close()