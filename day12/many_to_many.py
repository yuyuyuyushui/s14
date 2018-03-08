from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )#创建动态连接表

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


engine = create_engine("mysql+pymysql://root:111111@192.168.1.16/xzCMS",
                       encoding='utf-8')  # 第一步：建立数据库的连接

Base.metadata.create_all(engine)
