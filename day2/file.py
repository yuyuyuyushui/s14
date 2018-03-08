fle = open('yesterday', 'rwa')#文件的打开
line='new'
fle.read()#文件的读取
fle.readline()#文件的行的读取
fle.readlines()#返回迭代列表的文件行
fle.write(\n)#文件的写
fle.close()#文件的关闭
fle.tell()#查看光标字符指针的位置
fle.seek(0)#移动光标指针的位置，数字为指向地址
fle.flush()#刷新，将内存的内容写入硬盘
line.strip()#删除字符串的空白
continue#t跳出本次判断