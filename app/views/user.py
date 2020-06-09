#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:46
# @Author : xjm
# @Site : 
# @File : user.py
# @Software: PyCharm
from flask import Blueprint, abort, jsonify, redirect, url_for
from flask import request, render_template
from models.user import User
from models import db
from werkzeug.security import generate_password_hash
from settings import USER_CONFIG

blue = Blueprint('userBlue', __name__)


def check_user(name):  # 判断用户名是否能注册
    # user = User.query.get(name=name)  # 可能会报异常如果username不存在
    user = User.query.filter_by(name=name).first()
    if user:
        return False
    return True


def is_login_verity(name=None, auth_key=None):
    user = User.query.filter_by(name=name).first()
    if user:
        return user.check_pwd(auth_key)
    return False


def is_phone_verity(phone):
    user = User.query.filter_by(phone=phone).first()
    if user:
        return False
    return True


@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', None)
        auth_key = request.form.get('auth_key', None)
        if all((name, auth_key)):
            if is_login_verity(name, auth_key):
                return jsonify({'code': 200, 'msg': USER_CONFIG.get(200)})
            return jsonify({'code': 404, 'msg': USER_CONFIG.get(404)})
        return jsonify({"code": 10001, "msg": USER_CONFIG.get(10001)})
    return render_template('/user/login.html')


@blue.route('/register', methods=['POST'])
def register():
    user_info = {
        'name': request.form.get('name', None),
        'auth_key': request.form.get('auth_key', None),
        'nick_name': request.form.get('nick_name', None),
        'phone': request.form.get('phone', None),
    }
    user_info['auth_key'] = generate_password_hash(user_info['auth_key'])
    if check_user(user_info['name']):
        if is_phone_verity(user_info['phone']):
            user = User(**user_info)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('userBlue.login'))
        return jsonify({'code': 500, 'msg': USER_CONFIG.get(500)})
    return jsonify({'code': 403, 'msg': USER_CONFIG.get(403)})