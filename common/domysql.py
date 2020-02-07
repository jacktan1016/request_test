# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: domysql.py
@time: 2020/2/6 10:26
@desc: 
"""
import pymysql
from common.config import ReadConfig

class MysqlUtil:

    def __init__(self):
        conf = ReadConfig()
        host =conf.get("db","host")
        port =conf.getint("db","port") #这里一定要是getint,只写get报错
        user =conf.get("db","user")
        password =conf.get("db","password")
        self.mysql = pymysql.connect(host = host,port = port,user = user,password = password)
        self.cursor = self.mysql.cursor()

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__=="__main__":
    mysql = MysqlUtil()
    sql = "select MobilePhone from future.member ORDER BY MobilePhone desc limit 1"
    sql_0 = "select * from future.loan WHERE future.loan.MemberID={}".format(290670)
    sql_2 = "select Id from future.loan where MemberID=290670 order by CreateTime desc limit 1"
    res = mysql.fetch_one(sql_0)
    print(res)
    print(res[0])
    mysql.close()

    # mysql = pymysql.connect(host="test.lemonban.com",port=3306,user="test",password="test")#不写db ，可以直接在下面db.仓库
    # cursor = mysql.cursor()
    # sql = "select MobilePhone from future.member ORDER BY MobilePhone desc limit 1"
    # cursor.execute(sql)
    # res = cursor.fetchone()  # 最近的一个元组 ('18999999999',)
    # print(res[0],type(res[0]))
    #
    # # 游标关闭
    # cursor.close()

    # 数据库连接关闭
    # mysql.close()