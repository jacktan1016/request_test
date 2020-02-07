# -*- coding:utf-8 _*-
""" 
@author:jaketan
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 常量
"""
import os

#根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#datas目录
datas_dir = os.path.join(base_dir,"datas")

#xlsx路径
case_path = os.path.join(datas_dir,"cases.xlsx")

#conf的目录
conf_dir = os.path.join(base_dir,"conf")

#配置文件路径
test_path = os.path.join(conf_dir,"test.conf")
test2_path = os.path.join(conf_dir,"test2.conf")
global_path = os.path.join(conf_dir,"global.conf")

log_dir = os.path.join(base_dir,"log")

reports_dir = os.path.join(base_dir,"reports")

reports_html = os.path.join(reports_dir, 'reports.html')
testcases_dir = os.path.join(base_dir,"testcases")