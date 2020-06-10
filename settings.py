#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:34
# @Author : xjm
# @Site : 
# @File : settings.py
# @Software: PyCharm
import os

from redis import Redis


USER_CONFIG = {
    200: '用户验证成功',
    201: '用户名可使用',
    203: '用户注册成功',
    403: '用户名不可使用',
    404: '用户不存在或者密码错误',
    500: '手机号已被注册',
    501: '表单信息填写不全，请完善',
    10000: '用户不能为空',
    10001: '用户或密码不能为空'
}

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.join(PROJECT_DIR, 'app')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(STATIC_DIR, 'media')


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