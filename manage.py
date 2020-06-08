#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:34
# @Author : xjm
# @Site : 
# @File : manage.py.py
# @Software: PyCharm
from flask import render_template

from app import app
from flask_script import Manager, Server
from flask_cors import CORS
from app.views import user
# 必须要引入SQLALCHEMY设计的模型 创建才能成功
from models.user import User
from models import db


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/create_db')
def create_database():
    db.create_all()
    return "创建数据库中的所有模型表成功"


@app.route('/drop_db')
def drop_database():
    db.drop_all()
    return "删除库中所有模型类对应的表"


if __name__ == '__main__':
    # 解决跨域问题
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    app.register_blueprint(user.blue, url_prefix='/user')

    manager = Manager(app)
    manager.add_command("runserver", Server(use_debugger=True))
    manager.run()
