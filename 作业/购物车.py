goods_list = {
             'iphone6': {'price':6000,'num':10,'sum':10},
             'ipad': {'price':3000,'num':20,'sum':20},
             'mi4': {'price':2000,'num':43,'sum':40},
             'huawei6_plus': {'price':1999,'num': 8,'sum':8},
}


def loging(admin, pwd):
    with open('身份信息', 'r') as f:
        for i in f:
            admin1, pwd1, balance = i.strip().split()
            if admin == admin1 and pwd == pwd1:
                print('成功登录')
                return balance
        else:
            print("登陆失败")


def show_goods(goods_dict):
    print('序号'' 物品'' 价格'' 当前数量'" 产品总数")
    goods_list = {}
    num = 1
    for k in goods_dict:
        print(num, k, goods_dict[k]['price'], goods_dict[k]['num'], goods_dict[k]['num'])
        goods_list[num] = ([k, goods_dict[k]['price'], goods_dict[k]['num'], goods_dict[k]['num']])
        num += 1
    return goods_list


def buy_goods(shop_index, goods_dict):
    buy_goods_list = {}
    print('序号:%s'' 物品:%s'' 价格；%s'' 当前数量:%s'" 产品总数:%s" % (shop_index, goods_dict[shop_index][0], goods_dict[shop_index][1], goods_dict[shop_index][2],goods_dict[shop_index][3]))
    print('----------------------------------------------------------------------------------------------')
    flag_seconde = 1
    while flag_seconde:
        buy_num = input('请输入购买的数量>>：')
        print('----------------------------------------------------------------------------------------------')
        if buy_num == 'q':
            exit(0)
        if buy_num == 'b':
            break
        if int(buy_num) == 0:
            pass
        if int(buy_num) > 0 and int(buy_num) <= goods_dict[shop_index][3]:
            buy_goods_list[shop_index] = [goods_dict[shop_index][0], goods_dict[shop_index][1],goods_dict[shop_index][2], goods_dict[shop_index][3], buy_num]
            return buy_goods_list


def pay(price, num, money):
    money -= price*num
    if money < 0:
        m = input("若充值请输入Y")
        if m == 'q':
            exit(0)
        if m == "b":
            pass
        if m == 'y':
            recharge(money)


def recharge(money):
    num = input("请输入充值金额")
    money += num
    return money


def buy_car_show(good_list):
    show_all_sum = 0  ###初始化购物车商品总价###
    show_all_num = 0
    print('序号'' 物品'' 价格'' 当前数量'" 产品总数"' 购买数量')
    for i in good_list:
        print(i, good_list[i][0], good_list[i][1], good_list[i][2], good_list[i][3], good_list[i][4])
        show_all_num += 1
    return show_all_num
def cat_goods_modify(good_list, goods_list):


def buy_car(good_list,goods_list):
    if good_list == {}:
        print("购物车为空")
    else:
        buy_car_show(good_list)
        choice = input("请进行如下操作：修改C|继续购物")
        if choice == 'c':
            my_shop_cart,goods_list = cat_goods_modify(good_list,goods_list)
            goods_all_num = buy_car_show(my_shop_cart)

# admin = input('请输入用户名：')
# pwd  = input('请输入密码')
# change_money = loging(admin, pwd)
buy_goods_list = {}
first_flag = 1
while first_flag:
    # print(buy_goods_list)
    goods_dict = show_goods(goods_list)
    print('----------------------------------------------------------------------------------------------')
    shop_index = input('请输入商品编号|购物车(S)|余额充值(M)|结账(J)>>:')
    print('----------------------------------------------------------------------------------------------')
    if shop_index == 'q':
        exit(0)
    elif shop_index == 'm':  # 余额充值
        pass
    elif shop_index == 'j':
        pass
    elif shop_index == 's':  # 选择购物车
        buy_car(buy_goods_list)
    elif int(shop_index) in goods_dict:  # 选择商品编号
        buy_goods_list = buy_goods(int(shop_index), goods_dict)  # 传入商品编号，传入编号映射列表的字典
        print(buy_goods_list)
        print('----------------------------------------------------------------------------------------------')



