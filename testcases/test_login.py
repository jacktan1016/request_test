# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: testcases.py
@time: 2020/2/5 13:57
@desc: 测试用例集
"""
import unittest

from common import contants
from common.do_excel import Do_excel
from common.requests_pack import DoRequest
from ddt import ddt,data

@ddt
class LoginTest(unittest.TestCase):
    request = DoRequest()
    excel = Do_excel(contants.case_path)
    login_cases = excel.read_excel("login")

    def setUp(self) -> None:
        pass

    @data(*login_cases) # 利用*解包
    def test_login(self,login_case):  #login_case接受 解包的数据
        # print(login_case.id,login_case.method,login_case.expected)
        print("第{}条测试用例".format(login_case.id))
        print(login_case.method, login_case.url, login_case.data)
        res = self.request.request_p(login_case.method, login_case.url, login_case.data)
        try:
            self.assertEqual(res.text,login_case.expected,"login error")#执行不通过就login error
            self.excel.write_excel("login", login_case.id + 1, res.text, "pass")
            print("第{}条测试用例:通过".format(login_case.id))
        except AssertionError as e:
            self.excel.write_excel("login", login_case.id + 1, res.text, "fail")
            print("第{}条测试用例:失败".format(login_case.id))
            raise e



    def tearDown(self) -> None:
        pass