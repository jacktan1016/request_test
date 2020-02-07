# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: requests_pack.py
@time: 2020/2/5 11:48
@desc: requests的封装
"""
import requests,json
from common.config import ReadConfig
from common import logger



"""
查询天气
AppKey：9ac978932184a3f548ef3a496a0ee600
url:http://apis.juhe.cn/mobile/get   get方式
参数：	phone  key 

"""
logger = logger.get_logger("request")

class DoRequest:

    def __init__(self):
        self.session = requests.session()

    def request_p(self,method, url, data=None):
        method = method.upper()
        #为什么要在这里读取配置项，因为api_url写死了，可以直接封装
        config = ReadConfig()
        api_url = config.get("api","api_url")
        url = api_url+url
        print(method,url)
        if data is not None and type(data)==str:
            data = json.loads(data)
        if (method == "GET"):
            res = self.session.request(method,url =url,params=data)
            logger.info('response: {0}'.format(res.text))
        elif (method == "POST"):
            res = self.session.request(method,url = url,data=data)
            logger.info('response: {0}'.format(res.text))
        else:
            logger.error('Un-support method !!!')
            pass
        return res

    def close(self):
        self.session.close()


if __name__ == "__main__":
    request = DoRequest()
    url = r"http://test.lemonban.com/futureloan/mvc/api/member/login"
    data = {"mobilephone":"15810447656","pwd":"123456"}
    res =request.request_p("get",url,data)
    print(res.text)
    url_2 = r"http://test.lemonban.com/futureloan/mvc/api/loan/add"
    data_2 = {"memberId":290670, "title": "试试人品行不行，借个2W玩玩", "amount": 20000, "loanRate": "12.0", "loanTerm": 3,
            "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}
    res_1 = request.request_p("get",url_2,data_2)
    print(res_1.text)

