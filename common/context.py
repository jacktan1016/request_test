# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: context.py
@time: 2020/2/6 15:59
@desc: 
"""
# s目标字符串
# d替换的字符串

import re
from common.config import ReadConfig

conf = ReadConfig()


class Context:
    admin_user = conf.get("data", "admin_user")
    admin_pwd = conf.get("data", "admin_pwd")
    loan_member_id = conf.get("data","loan_member_id")  # 固定一个借款人ID
    normal_user = conf.get("data","normal_user") #投资人
    normal_pwd = conf.get("data","normal_pwd")
    normal_member_id = conf.get("data","normal_member_id")

def replace(s, d):
    p = "\${(.*?)}"
    while re.search(p, s):
        key = re.search(p, s).group(1)
        value = d[key]
        s = re.sub(p, value, s, count=1)  # 找到一个就替换一个
    return s


def replace_new(s):
    p = "\${(.*?)}"
    while re.search(p, s):
        key = re.search(p, s).group(1)
        if hasattr(Context,key):
            value = getattr(Context,key)
            s = re.sub(p, value, s, count=1)  # 找到一个就替换一个
        else:
            print("没有这个属性:{}".format(key))
            return None
    return s


s = '{"mobilephone":"${admin_user}","admin_pwd":"${admin_pwd}"}'
# d = {"mobilephone": "18672687411", "admin_pwd": "123456"}
# new = replace(s, d)
# print(new)
new  = replace_new(s)
print(new)