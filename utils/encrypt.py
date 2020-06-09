#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/6/9 11:44
# @Author : xjm
# @Site : 
# @File : encrypt.py
# @Software: PyCharm
import hashlib


def encrypt(word):
    # 将明文的word转成md5格式的密文
    md5_ = hashlib.md5()
    md5_.update(word.encode('utf-8'))
    md5_.update('@youjia4321@8888#$*%'.encode('utf-8'))
    return md5_.hexdigest()


if __name__ == '__main__':
    print(encrypt('000000'))
