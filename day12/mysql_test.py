import pymysql

conn = pymysql.connect(host='192.168.1.16', port=3306, user='root', passwd='111111', db='xzCMS')#建立连接
cursor = conn.cursor()#创建游标
# effect_row = cursor.execute("select * from student")
# print(cursor.fetchone())
# print(cursor.fetchall())

#effect_row = cursor.execute("update host set host = '1.1.1.2' where nid > %s",(1,))
# print(effect_row)
date = [
    ("N1", "34", "2017-07-09"),
    ("N2", "44", "2017-09-10"),
    ("N3", "55", "2017-12-12")

]
cursor.executemany("insert into student (name,age, register_date) values(%s,%s,%s)", date)
conn.commit()
cursor.close()
