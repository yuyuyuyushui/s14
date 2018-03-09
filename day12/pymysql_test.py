import pymysql

mysql_info ={
    'host':'10.1.1.2',
    'port':"3306",
    'user':"root",
    "passwd":"111111",
    'db': '***',
    'charset':'utf-8'
}
class MysqlUtil:
    def __init__(self):
        self.db_info = mysql_info
        self.conn = self.__getConnect()
    def __getConnect(self):# 封装数据库的连接
        try:
            conn = pymysql.connect(self.db_info)
            return conn
        except Exception as e:
            print("数据库连接异常：%s" %e)

    def sql_execute(self, sql):#数据库语句执行
        conn = self.__getConnect()
        curs = conn.cursor()# 创建游标对象
        try:
            mysql_ = curs.execute(sql)
        except Exception as e:
            conn.rollback()# 出现异常就回滚
            print("执行数据库出错：%s" % e)
        else:
            curs.close()# 关闭游标
            conn.commit()# 无异常时提交
            # return mysql_
    def mysql_getrows(self, sql):#返回查询结果
        conn = self.__getConnect()
        curs = conn.cursor()  # 创建游标对象
        try:
            mysql_ = curs.execute(sql)
        except Exception as e:
            conn.rollback()# 出现异常就回滚
            print("执行数据库出错：%s" % e)
        else:
            rows = curs.fechall()
            curs.close()
            return rows