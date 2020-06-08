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

app = Flask(__name__, static_folder='static', static_url_path='/s')
app.config.from_object(settings.Dev)

# 初始化数据库
db.app = app
db.init_app(app=app)

