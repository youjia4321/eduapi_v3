#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:33
# @Author : xjm
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm

from flask import Flask
import settings
from models import db
from flask.logging import default_handler
import logging

app = Flask(__name__, static_folder='static', static_url_path='/s')
app.config.from_object(settings.Dev)

# 初始化数据库
db.app = app
db.init_app(app=app)

app.logger.removeHandler(default_handler)  # 移除app默认的handler
app.logger.setLevel(logging.INFO)  # 设置日志记录等级

fmt = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

file_handler = logging.FileHandler('edu.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(fmt)

app.logger.addHandler(file_handler)

