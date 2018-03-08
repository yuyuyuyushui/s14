import copy

lst = ['luo', ['zhi', 56]]
#lst.append('qiang') #列表的增
#lst.index('luo') #查
#lst.insert(1,'qiang')#插入
#lst.pop(1)#删除
#del lst[0]#
for i in enumerate(lst):
    print(i)#提供lst的序列号和对应的值，用于循环遍历
    num = input("please")
    if num.isdigit():#数字的判断
