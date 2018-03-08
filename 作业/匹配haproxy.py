def check(date):
    with open("haproxy配置文件", 'r', encoding='utf-8') as f:
        f_list = f.readlines()
        addr = "backend %s\n"%date
        for index ,value in enumerate(f_list):
            if addr == value:
                print("你已经找到你输入的网址")
                print(f_list[index+1])
                return 1
        else:
            print("没找到")


def write(date2,date3):
    addr1 = "\nbackend %s" %date2
    addr2 = "\n        %s"%date3

    addr_list = [addr1, addr2]
    with open("haproxy配置文件",'a',encoding='utf-8') as f:
        f.writelines(addr_list)
        print("添加成功")
if __name__ == '__main__':
    choice = input("请输入：1.查询，2.增加>>:")
    if int(choice) == 1:
        date = input("请输入你要查询的网址")
        check(date)
    if int(choice) == 2:
        date2 = input("请输入你要增加的网址")
        date3 = input("请输入你要增加的字段")
        if check(date2)==1:
            print("你增加的网址在程序中")
        else:
            write(date2,date3)







