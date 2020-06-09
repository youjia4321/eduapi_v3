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


# 模型之间的关系不需要创建第三个模型类实现第三张关系表创建
# 创建用户和角色的关系表
user_role = db.Table('t_user_role',
                     db.Column('uid', db.Integer, db.ForeignKey('t_user.id', name='user_fk')),
                     db.Column('rid', db.Integer, db.ForeignKey('t_role.id', name='role_fk')))


class BaseModel(db.Model):
    __abstract__ = True  # 作用：不会作为普通模型的创建对应的表(抽象模型)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)


# 继承BaseModel：
class Role(BaseModel):  # 用户角色
    __tablename__ = 't_role'  # 设置数据库中的表名(默认为当前类名的小写)

    def __repr__(self):
        return '<Role %r>' % self.name


class Permission(BaseModel):  # 用户权限
    __tablename__ = 't_permission'

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):  # 用户
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    auth_key = db.Column(db.String(255), nullable=False)
    nick_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20), unique=True, nullable=False)
    photo = db.Column(db.String(255), default="/s/media/avatar.jpg")
    join_time = db.Column(db.DateTime, index=True, default=datetime.now, nullable=False)  # 设置索引index=True

    # rid = db.Column(ForeignKey('t_role.id'))
    # Many-to-Many 多对多的关系，指定secondary设置关联的表，Table()
    roles = db.relationship(Role, secondary=user_role)

    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, auth_key):
        return check_password_hash(self.auth_key, auth_key)
