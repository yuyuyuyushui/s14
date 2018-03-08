import time
import datetime
import random
import os#提供对操作系统进行调用的接口

v=time.time()
x=time.localtime()
y=time.strftime("%Y-%m-%d %H:%M:%S", x)#元祖转换为正常表达时间
z=time.strptime('2017-12-14 23:10:11', '%Y-%m-%d %H:%M:%S')#正常时间表达转换为元祖
print()#时间戳=1970+秒
print(time.localtime())#元祖
print(x[2]);print(x.tm_mon)#元祖中元素获取的方法
print(time.asctime(x))#将一个元祖---->Thu Dec 14 23:24:15 2017这种表示方法
print(time.ctime(v))#将时间戳----->Thu Dec 14 23:28:22 2017这种表示方法
print(z)
print(y)
print(time.timezone)


print(datetime.datetime.now())#获取当前时间
print(datetime.datetime.now()+datetime.timedelta(3))#当前时间加三天
print(datetime.datetime.now()+datetime.timedelta(hours=3))#当前时间加三小时

print(random.random())#随机0-1中的数
print(random.randint(1,3))#随机【1-3】的整数，左闭右闭
print(random.randrange(1,3))#随机数，左闭右开
print(random.choice('look'))#随机的选一个字母

print(chr(65))#ASCii码数字转换为字母

print(os.getcwd())#湖区当前工作目录
print(os.curdir)#返回当前目录
print(os.pardir)#获取当前目录的上一级
print(os.chdir(r'C:'))#切换当前路径
print(os.makedirs(r'C:\a\b\c'))#递归的创建没有父目录的子目录
print(os.removedirs(r'C:\a\b\c'))#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，以此类推
#print(os.mkdir(r'D:\a'))#添加一个目录
#print(os.rmdir(r'D:\a'))#删除一个目录
#print(os.mknod(r'D:\a\j.txt'))#创建文件
print(os.listdir(r'D:'))#当前目录下的列表
print(os.stat(r'D:\a'))#获取当前路径文件的属性；win下为\\分隔符
print(os.sep)#win下的\\路径分隔符
print(os.linesep)#输出当前平台使用的终止分隔符，换行分隔符
print(os.pathsep)#输出用于分割文件路径的字符串
print(os.environ)#查看当前的环境变量，win下用:为分隔符
print(os.name)#输出当前系统名
print(os.system('ipconfig'))#调用系统命令
print(os.path.split(r'D:\a\j.txt'))#将目录和文件分开
print(os.path.dirname(r'D:\a\j.txt'))#将文件的上一级目录返回
print(os.path.exists(r'D:\a'))#判断路径是否存在
print(os.path.isabs(r'D:\a'))#判断是否绝对路径