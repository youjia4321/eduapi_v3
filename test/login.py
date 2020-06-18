#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/18 11:36
# @Author : xjm
# @Site : 
# @File : login.py
# @Software: PyCharm

from unittest import TestCase
import requests


class TestUser(TestCase):
    def test_login(self):
        user_info = {
            'name': 'wxy',
            'auth_key': '000000',
        }

        resp = requests.post("http://localhost:5000/user/login", data=user_info)

        print(resp.json())

        self.assertEqual(resp.json()['code'], 200, '请求失败')