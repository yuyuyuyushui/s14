import hashlib

def md5(arg):         #传入变量
    md5_pwd = hashlib.md5(bytes('你好', encoding='utf-8'))
    md5_pwd.update(bytes(arg, encoding='utf-8'))
    return  md5_pwd.hexdigest()#返回加密数据
def log(user,pwd):
    with open('db.txt','r',encoding='utf-8') as f:
        for i in f:
            u,p =i.strip().split('|')
            if u == user and p == md5(pwd):
                return True
def register(user, pwd):
    with open('db.txt','a+',encoding='utf-8') as f:
        f.seek(0, 0)#移动指针位置
        for i in f.readlines():
            u, p = i.strip().split('|')
            #print(i)
            if user == u:
                return 0
            else:
                continue
        temp = user+'|'+md5(pwd)+'\n'
        f.write(temp)
while(1):
    i = input('1表示登陆，2表示注册：')
    if i == '2':
        users = input('用户名：')
        pwds = input('密码：')
        new = register(users,pwds)
        if new == 0:
            print('用户名已注册，请重新输入')
            break
    elif i == '1':
        user = input('用户名：')
        pwd = input('密码：')
        r =log(user,pwd)

        if  r == True:
            print('登陆成功:')
            break
        else:
            print('登陆失败：')
            break
