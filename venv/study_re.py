# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: study_re.py
@time: 2020/2/6 15:10
@desc: 正则温习
"""
import json
# phone =18672687411
# pwd =123456
# s = '{"mobilephone":"${admin_user}","admin_pwd":"${admin_pwd}"}'
# 处理了2次比较麻烦
# s_dict = json.loads(s)
# if s_dict["mobilephone"]=="${admin_user}":
#     s_dict["mobilephone"] = phone
# if s_dict["admin_pwd"]=="${admin_pwd}":
#     s_dict["admin_pwd"] = pwd
# print(s_dict)
import re
import requests
# p = "\${(.*?)}"
# v = re.search(p,s)
# g = v.group()
# print(g)
# new  = re.sub(p,"123456",s,count=1)  #count =0 匹配全部,1表示只匹配1次
# print(new)
# class Girl:
#
#     hobby = None
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def singe(self):
#         print(self.name+"会唱歌")
#
# girl = Girl("lili",18)
# print(girl.name)
# setattr(girl,"sex","女") #给类动态添加属性或者方法
# print(girl.sex)
#
# setattr(Girl,"hub","swimming")
# print(getattr(Girl,"hub"))
# print(hasattr(Girl,"hobby"))
# delattr(Girl,"hub")
# delattr(girl )

url = r"http://test.lemonban.com/futureloan/mvc/api/loan/add"
data = {"memberId":97,"title":"试试人品行不行，借个2W玩玩","amount":20000,"loanRate":"12.0","loanTerm":3,"loanDateType":0,"repaymemtWay":11,"biddingDays":5}
res = requests.post(url,data=data)
print(res.text)