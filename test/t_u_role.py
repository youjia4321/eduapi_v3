#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/9 16:01
# @Author : xjm
# @Site : 
# @File : t_u_role.py
# @Software: PyCharm
from app import app
from models.user import User, Role, Permission, user_role, db
from werkzeug.security import generate_password_hash


def add_user():
    u1 = User()
    u1.phone = '1008611'
    u1.name = 'wsy'
    u1.nick_name = '宥嘉'
    u1.auth_key = generate_password_hash('000000')

    u2 = User()
    u2.phone = '10086'
    u2.name = 'xjm'
    u2.nick_name = '文乐'
    u2.auth_key = generate_password_hash('000000')

    # db.session.add(u1) # 提交单个
    db.session.add_all((u1, u2))  # 多个
    db.session.commit()
    print('提交之后的User-Id：', u1.id, u2.id)


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')

    # 批量添加
    db.session.add_all((r1, r2))
    db.session.commit()
    print(r1.id, r2.id)


def add_user_role():
    # db.Table()不能作为模型类使用
    # db.session.add_all((
    #     user_role(user_id=1, role_id=1),
    #     user_role(user_id=2, role_id=1),
    #     user_role(user_id=2, role_id=2)
    # ))

    # 为用户ID为1的用户增加'系统管理员'角色
    u = User.query.get(1)

    admin_role = Role.query.filter(Role.name.__eq__('系统管理员')).one()
    print(u.nick_name, admin_role.name)

    # 将角色对象添加给用户
    u.roles.append(admin_role)
    db.session.commit()
    print('ok')


def query_user_role(user_id=1):
    u = User.query.get(user_id)
    print('------%s：拥有的角色------' % u.nick_name)
    for role in u.roles:
        print(role.name)


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)

    # add_user()
    # add_role()
    # add_user_role()
    query_user_role()