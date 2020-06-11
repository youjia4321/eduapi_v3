#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/10 20:56
# @Author : xjm
# @Site : 
# @File : t_log.py
# @Software: PyCharm
import logging
from logging import StreamHandler, FileHandler
from logging.handlers import HTTPHandler

from logging import Formatter

logger = logging.getLogger('edu_api')


def config_log():
    fmt = Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    io_handler = StreamHandler()
    io_handler.setLevel(logging.DEBUG)
    io_handler.setFormatter(fmt)

    file_handler = FileHandler('edu_logs.log')
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(fmt)

    http_handler = HTTPHandler(host='localhost:5000',
                               url='/log',
                               method='POST')
    http_handler.setLevel(logging.ERROR)
    http_handler.setFormatter(fmt)  # 上传的数据不需要formatter

    logger.setLevel(logging.DEBUG)
    logger.addHandler(io_handler)
    logger.addHandler(file_handler)
    logger.addHandler(http_handler)


config_log()
logger.info('您好， 我是Disen!')
logger.warning('你的余额不足500元， 请尽快充值！')
logger.error('你的服务器被攻击了12000次，严重影响你的客户心情，请尽快处理！')
logger.critical('你的9080端口检查出来存在1000个恶意程序请求')
