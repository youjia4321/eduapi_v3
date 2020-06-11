#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/10 20:19
# @Author : xjm
# @Site : 
# @File : logger.py
# @Software: PyCharm
from flask import Blueprint, request, jsonify

blue = Blueprint('loggerBlue', __name__)


@blue.route('/log', methods=['POST'])
def upload_log():
    print(request.form)
    return jsonify({
        'msg': 'ok'
    })