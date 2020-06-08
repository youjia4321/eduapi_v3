#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/5 19:07
# @Author : xjm
# @Site : 
# @File : user.py
# @Software: PyCharm
from werkzeug.security import check_password_hash
from models import db
from datetime import datetime


class User(db.Model):  # 用户
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    auth_key = db.Column(db.String(255), nullable=False)
    nick_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20), unique=True, nullable=False)
    photo = db.Column(db.String(255), default="/s/media/avatar.jpg")
    join_time = db.Column(db.DateTime, index=True, default=datetime.now, nullable=False)  # 设置索引index=True

    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, auth_key):
        return check_password_hash(self.auth_key, auth_key)


class BaseModel(db.Model):
    __abstract__ = True  # 作用：不会作为普通模型的创建对应的表(抽象模型)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)


# 继承BaseModel：
class Role(BaseModel):  # 用户角色
    def __repr__(self):
        return '<Role %r>' % self.name


class Permission(BaseModel):  # 用户权限
    def __repr__(self):
        return '<Role %r>' % self.name

