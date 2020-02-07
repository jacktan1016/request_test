# -*- coding:utf-8 -*-
"""
@author: JakeTan
@file: logger.py
@time: 2020/2/5 13:36
@desc: 日志的封装
"""
import logging
import logging.handlers
import os

"""
info debug warn error 
"""
from common import contants
from common.config import ReadConfig

config = ReadConfig()
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel('DEBUG') # 直接设置为最低
    # 定义输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)

    file_name = os.path.join(contants.log_dir, 'case.log')
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10)
    level = config.get('log', 'file_handler')
    file_handler.setLevel(level)
    file_handler.setFormatter(formate)

    console_handler = logging.StreamHandler()
    level = config.get('log', 'console_handler')
    console_handler.setLevel(level)
    console_handler.setFormatter(formate)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger("request_pp")
    logger.debug("hahha")
