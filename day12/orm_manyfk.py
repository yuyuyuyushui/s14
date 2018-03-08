from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,sessionmaker


Base = declarative_base()  # 第二步：生成orm基类


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer, ForeignKey("address.id"))  # 账单地址
    shipping_address_id = Column(Integer, ForeignKey("address.id"))  # 邮寄地址

    billing_address = relationship("Address", foreign_keys=[billing_address_id])  # 相互连接
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__= 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return self.street
engine = create_engine("mysql+pymysql://root:111111@192.168.1.16/xzCMS",
                       encoding='utf-8')  # 第一步：建立数据库的连接

Base.metadata.create_all(engine)
