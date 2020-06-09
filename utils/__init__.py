#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:33
# @Author : xjm
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
from redis import Redis


# redis数据库对象
rd = Redis(host='localhost', port=6379, password='123456', db=2, decode_responses=True)
