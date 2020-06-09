#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/8 16:55
# @Author : xjm
# @Site : 
# @File : register.py
# @Software: PyCharm

from unittest import TestCase
import requests


class TestUser(TestCase):
    def test_register(self):
        user_info = {
            'name': 'wsy',
            'auth_key': '123456',
            'nick_name': '王大大',
            'phone': '1008611'
        }

        resp = requests.post("http://localhost:5000/user/register", data=user_info)

        print(resp.json())

        self.assertEqual(resp.json()['code'], 203, '请求失败')



