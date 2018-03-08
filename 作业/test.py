class Book(object):

    def __init__(self, title,name):
        self.title = title
        self.name = name

    def clsp(self):
        return self.name
    def seed(self):
        return self.clsp()
    @classmethod
    def create(cls, ss):
        new = ss
        return new
    def __str__(self):
        return 'nihao'
# book1 = Book("python",'luo')
# book2 = Book.create("python and django", 'liu')
# print(book1)
# list1 = 'hjgjh'
#
# r, l = list1.split('g')
# print(type(list1.split('g')))
print(Book.create('ss'))