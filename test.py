# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 10:41
# @Author  : Toby
# @Site    : 
# @File    : test.py
# @Software: PyCharm

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
