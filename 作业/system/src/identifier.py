import pickle, os
from lib import commons
from confing import setting
class Nid:
    def __init__(self, db_path):
        self.uid = commons.create_md5()
        self.db_path = db_path

    def __str__(self):
        return self.uid

    def get_ID_obj(self):
        for id in os.listdir(self.db_path):
            if self.uid == id:
                return pickle.load(open(os.path.join(self.db_path,self.uid), 'rb'))