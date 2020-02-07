# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: config.py
@time: 2020/2/5 15:39
@desc: 封装配置文件
"""
import configparser
from common import contants
class ReadConfig:

    def __init__(self):
        # 实例化对象
        self.conf = configparser.ConfigParser()
        # 读取文件，其实就是加载文件
        self.conf.read(contants.global_path)
        open = self.conf.getboolean("switch","open")
        if open:
            self.conf.read(contants.test_path,encoding="utf-8")
        else:
            self.conf.read(contants.test2_path,encoding="utf-8")

    #用我的实例，调用我的方法---实际获取读取global_dir之后的conf
    def get(self,section,option):
        return self.conf.get(section=section,option=option)

    def getboolean(self,section,option):
        return self.conf.getboolean(section=section, option=option)

    def getint(self,section,option):
        return self.conf.getint(section=section, option=option)




if __name__=="__main__":
    config = ReadConfig()
    api_url = config.get("api","api_url")
    print(api_url)

    # conf = configparser.ConfigParser()
    # from common import contants
    # conf.read(contants.global_path)
    # open = conf.getboolean("switch","open")
    # if open:
    #     conf.read(contants.test_path)
    # else:
    #     conf.read(contants.test2_path)