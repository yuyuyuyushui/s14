name = [1, 2, 2, 3]
def chage_list():
    name[0] = 'luo'
chage_list()#局部列表，字典，可以改变全局变量，数字和字符串不能
print(name)