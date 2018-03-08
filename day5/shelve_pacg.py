# import shelve
# import datetime
#
# # fle = shelve.open('shelve_test')
# # name = {'luo':'qiang', 'liu':'wei'}
# # info = {'age':'23', 'ages':33}
# # fle['name'] = name
# # fle['info'] = info
# # fle['datetime'] = datetime.datetime.now()
#
# d = shelve.open('shelve_test')
# print(d.get('name'))
# print(d.get('info'))
# print(d.get('datetime'))
with open('db.txt', 'a+', encoding='utf-8') as f:
    # for i in f():
    #     u, p = i.strip().split('|')
    #     print(i)
    f.seek(0,0)
    print(f.read())

