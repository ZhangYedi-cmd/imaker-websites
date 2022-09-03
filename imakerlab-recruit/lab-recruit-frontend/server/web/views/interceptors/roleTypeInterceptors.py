#!/usr/bin/python3.6
# @Time    : 2021/9/25 13:48
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : roleTypeInterceptors.py
# ImakerLab-Website-Flask

'''
roleType 认证
如果是未审核的导师请求, 则业务不进行
'''
from flask import g


def check_role_type():
    tutor = g.tutor
    if tutor.status == '未通过':
        return
    return None
