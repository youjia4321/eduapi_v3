#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:34
# @Author : xjm
# @Site : 
# @File : settings.py
# @Software: PyCharm
from redis import Redis


USER_CONFIG = {
    200: '用户验证成功',
    404: '用户不存在或者密码错误',
    10001: '账户或密码不能为空'
}


class Dev(object):
    ENV = 'development'  # 开发环境配置 默认环境(production)
    DEBUG = True
    SECRET_KEY = 'daj@jwfn231%lodsdai#@'

    # 配置session 存储信息的地方
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='127.0.0.1', port=6379, password='123456', db=2)

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/eduapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 可扩展
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 回收资源时自动提交事务
    SQLALCHEMY_ECHO = False  # 显示调用SQL