#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/4 20:46
# @Author : xjm
# @Site : 
# @File : user.py
# @Software: PyCharm
import uuid
from datetime import datetime, timedelta
from flask import Blueprint, abort, jsonify, redirect, url_for
from flask import request, render_template
from models.user import User
from models import db
from werkzeug.security import generate_password_hash
from settings import USER_CONFIG
from utils import cache

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
        if user.check_pwd(auth_key):
            return user
    return None


def is_phone_verity(phone):
    user = User.query.filter_by(phone=phone).first()
    if user:
        return False
    return True


@blue.route('/name/verity', methods=['POST'])
def verity_name():
    name = request.form.get('name', '')
    if len(name.strip()) == 0:
        return jsonify({'code': 10000, 'msg': USER_CONFIG.get(10000)})
    if check_user(name):
        return jsonify({'code': 201, 'msg': USER_CONFIG.get(201)})
    return jsonify({'code': 403, 'msg': USER_CONFIG.get(403)})


@blue.route('/logout', methods=['GET'])
def logout():
    resp = redirect('/user/login')
    resp.delete_cookie('token')
    token = request.cookies.get('token')
    cache.clear_token(token)
    return resp


@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', None)
        auth_key = request.form.get('auth_key', None)
        if all((name, auth_key)):
            login_user = is_login_verity(name, auth_key)
            if login_user:
                # 登录成功 生成token
                token = uuid.uuid4().hex
                # 将token添加到redis，token->user_id
                cache.save_token(token, login_user.id)
                return jsonify({'code': 200, 'token': token, 'msg': USER_CONFIG.get(200)})
            return jsonify({'code': 404, 'msg': USER_CONFIG.get(404)})
        return jsonify({"code": 10001, "msg": USER_CONFIG.get(10001)})
    return render_template('/user/login.html')


@blue.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', None),
        auth_key = request.form.get('auth_key', None)
        nick_name = request.form.get('nick_name', None)
        phone = request.form.get('phone', None)
        if all((name, auth_key, nick_name, phone)):
            user_info = {
                'name': name,
                'auth_key': auth_key,
                'nick_name': nick_name,
                'phone': phone
            }
            user_info['auth_key'] = generate_password_hash(user_info['auth_key'])
            if is_phone_verity(user_info['phone']):
                user = User(**user_info)
                db.session.add(user)
                db.session.commit()
                return jsonify({'code': 203, 'msg': USER_CONFIG.get(203)})
            return jsonify({'code': 500, 'msg': USER_CONFIG.get(500)})
        return jsonify({'code': 501, 'msg': USER_CONFIG.get(501)})
    return render_template('/user/register.html')