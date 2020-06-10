#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/9 14:06
# @Author : xjm
# @Site : 
# @File : cache.py
# @Software: PyCharm
from utils import rd


def save_token(token, user_id):
    # 保存token及对应的user_id
    # 在redis数据库存储token -> user_id 信息，设置过期时间ex
    rd.set(token, user_id, ex=3*24*3600)
    # rd.expire(token, 3*24*3600)


def get_user_id(token):
    return rd.get(token)


def clear_token(token):
    rd.delete(token)
