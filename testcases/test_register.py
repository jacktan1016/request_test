# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: test_register.py
@time: 2020/2/5 23:26
@desc: 
"""
import unittest

from common import contants
from common.do_excel import Do_excel
from common.requests_pack import DoRequest
from ddt import ddt, data
from common.domysql import MysqlUtil
import json

@ddt
class RegisterTest(unittest.TestCase):
    excel = Do_excel(contants.case_path)
    login_cases = excel.read_excel("register")

    @classmethod
    def setUpClass(cls):  # 类方法，类里面只允许运行一次，setUP 每一个方法运行前都要运行
        cls.request = DoRequest()
        cls.mysql = MysqlUtil()
        sql = "select MobilePhone from future.member ORDER BY MobilePhone desc limit 1"
        cls.max = cls.mysql.fetch_one(sql)[0]

    @data(*login_cases)  # 利用*解包
    def test_login(self, login_case):  # login_case接受 解包的数据
        # print(login_case.id,login_case.method,login_case.expected)
        data_dict = json.loads(login_case.data)
        if data_dict["mobilephone"]=="${register_mobile}":
            data_dict["mobilephone"] = int(self.max)-100882
        print("第{}条测试用例".format(login_case.id))
        print(login_case.method, login_case.url, data_dict)
        res = self.request.request_p(login_case.method, login_case.url, data_dict)
        try:
            self.assertEqual(res.text, login_case.expected, "reqister error")  # 执行不通过就login error
            self.excel.write_excel("register", login_case.id + 1, res.text, "pass")
            print("第{}条测试用例:通过".format(login_case.id))
        except AssertionError as e:
            self.excel.write_excel("register", login_case.id + 1, res.text, "fail")
            print("第{}条测试用例:失败".format(login_case.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        cls.mysql.close()
