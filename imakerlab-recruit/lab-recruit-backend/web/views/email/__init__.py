#!/usr/bin/python3.6
# @Time    : 2021/8/28 10:46
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : __init__.py
# ImakerLab-Website-Flask


from flask import Blueprint

email_route = Blueprint(__name__, "email_route")
from .email import *
