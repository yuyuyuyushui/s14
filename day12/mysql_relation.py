import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("mysql+pymysql://root:111111@192.168.1.16/xzCMS",
                       encoding='utf-8')  # 第一步：建立数据库的连接

Base = declarative_base()  # 第二步：生成orm基类


class Student(Base):  # 第三步：创建表的结构
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "day:%s name:%s"%(self.student.day, self.name)


class StudyRecord(Base):  # 第三步：创建表的结构
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(String(32), nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))  # 创建外部键的关联

    def __repr__(self):
        return "%s day: %s status: %s" % (self.student.name, self.day, self.status) #Student.name可以关联另一张表的名

    student = relationship("Student", backref="my_study_record")#student通过backref里的值关联StudyRecord，
Base.metadata.create_all(engine)  # 第四步：创建表结构
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# s1 = Student(name='Du', register_date='2016-08-09')  # 第五步：写入数据
# s2 = Student(name='Luo', register_date='2016-10-09')
# s3 = Student(name='Zhang', register_date='2016-11-09')
#
# study_obj1 = StudyRecord(day=1, status='Yes', stu_id=1)
# study_obj2 = StudyRecord(day=2, status='Yes', stu_id=1)
# study_obj3 = StudyRecord(day=3, status='Yes', stu_id=3)
# study_obj4 = StudyRecord(day=1, status='Yes', stu_id=2)
# Session.add_all([s1,s2,s3,study_obj1,study_obj2,study_obj3,study_obj4])  # 第五步：把要创建的数据对象添加到这个session里， 一会统一创建
stu_obj = Session.query(Student).filter(Student.name == "Du").first()
print(stu_obj.my_study_record)
Session.commit()