class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating'%self.name)

    def sleep(self):
        print('%s is sleeping'%self.name)


class Relation(object):

    def make_frients(self,obj):
        print("%s is made fients with %s"%(self.name,obj.name))


class Man(People, Relation):#从左至右执行
        #def __init__(self,name,age,money):
    #super(Man, self).__init__(name, age)#新式类的写法
        #self.money = money
        #print('%s have 100 kuai'%self.name)

    def sleep(self):#重构父类
        People.sleep(self)
        print('man is sleeping')


class Woman(Relation,People):#继承母类
    def born(self):
        print('%s is borning '%self.name)



m1 = Man('duyonsgehng',22)
m2 = Woman('chengronghua', 23)
m1.make_frients(m2)