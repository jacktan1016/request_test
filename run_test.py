# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: run_test.py
@time: 2020/2/6 22:55
@desc:  执行运行文件
"""
from common import contants
import  unittest
from libext import  HTMLTestRunnerNew
# 自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(contants.testcases_dir, pattern="test_*.py", top_level_dir=None)
#
with open(contants.reports_html, 'wb+') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='Mongo')
    runner.run(discover)  # 执行查找到的用例