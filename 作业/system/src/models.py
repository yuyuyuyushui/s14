import pickle, time, os
from lib import commons
from confing import setting
from src import identifier


class Base:
    def save(self):
        path_file = os.path.join(self.db_path, str(self.id))
        pickle.dump(self, open(path_file, 'wb'))
        print(path_file)
class School(Base):
    db_path = setting.SCHOOL_DB
    def __init__(self, name, addr):
        self.id = identifier.schoolNid(School.db_path)
        self.name = name
        self.addr = addr

    def __str__(self):
        return self.name

    @staticmethod
    def find_all():
        school_lst = []
        for item in os.listdir(os.path.join(School.db_path)):
            obj_school = pickle.load(open(os.path.join(School.db_path, item), 'rb'))

            school_lst.append(obj_school)
        return school_lst
class Course:
    def __init__(self, name):
        self.name = name
class Teachear:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name
s = School('py', 'chongqi')
print(s.db_path)
s.save()
print(s.find_all())