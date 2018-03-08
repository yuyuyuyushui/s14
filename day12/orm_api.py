#此文件用于创建文件以及增删改查
from day12 import orm_manyfk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_manyfk.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# addr1 = orm_manyfk.Address(street="ChunXilu", city="Chengdu", state="SiChuan")
# addr2 = orm_manyfk.Address(street="Dahualu", city="MianYang", state="ChongQing")
# addr3 = orm_manyfk.Address(street="Pizian", city="JiangYou", state="HuangDu")
#
# session.add_all([addr1, addr2, addr3])
# c1 = orm_manyfk.Customer(name="Jack", billing_address=addr1, shipping_address=addr2)#关联地址
# c2 = orm_manyfk.Customer(name="Luo", billing_address=addr3, shipping_address=addr3)
#
# session.add_all([c1, c2])
obj = session.query(orm_manyfk.Customer).filter(orm_manyfk.Customer.name=="Jack").first()#过滤Jack时，过滤所有所对的值
print(obj.name, obj.billing_address, obj.shipping_address)
session.commit()
