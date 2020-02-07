# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: test_invest.py
@time: 2020/2/6 17:23
@desc: 
"""
import unittest

from common import contants
from common.do_excel import Do_excel
from common.requests_pack import DoRequest
from libext.ddtnew import ddt,data
from common.domysql import MysqlUtil
import json
from common.context import Context
from common import context
from common import logger

logger =logger.get_logger("testcase")
@ddt
class InvestTest(unittest.TestCase):
    excel = Do_excel(contants.case_path)
    login_cases = excel.read_excel("invest")

    @classmethod
    def setUpClass(cls):  # 类方法，类里面只允许运行一次，setUP 每一个方法运行前都要运行
        cls.request = DoRequest()
        cls.mysql = MysqlUtil()
        # sql = "select MobilePhone from future.member ORDER BY MobilePhone desc limit 1"
        # cls.max = cls.mysql.fetch_one(sql)[0]

    @data(*login_cases)  # 利用*解包
    def test_login(self, login_case):  # login_case接受 解包的数据
        # print(login_case.id,login_case.method,login_case.expected)
        #查找参数化数据，进行动态替换
        str_data = context.replace_new(login_case.data)
        logger.info("第{}条测试用例".format(login_case.id))
        logger.info("测试method,测试url,data:",login_case.method, login_case.url, str_data)
        res = self.request.request_p(login_case.method, login_case.url, str_data)
        try:
            self.assertEqual(res.json()["code"], login_case.expected, "invest error")  # 执行不通过就login error
            self.excel.write_excel("invest", login_case.id + 1, res.text, "pass")
            if res.json()["msg"]=="加标成功":
                loan_member_id =getattr(Context,"loan_member_id")
                print(loan_member_id)
                sql = "select Id from future.loan order by CreateTime desc limit 1"
                print("sql是.....",self.mysql.fetch_one(sql))
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context,"loan_id",str(loan_id))

            logger.info("第{}条测试用例:通过".format(login_case.id))
        except AssertionError as e:
            self.excel.write_excel("register", login_case.id + 1, res.text, "fail")
            logger.info("第{}条测试用例:失败".format(login_case.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        cls.mysql.close()