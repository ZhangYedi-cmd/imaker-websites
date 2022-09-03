#!/usr/bin/python3.6
# @Time    : 2021/8/20 22:20
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : __init__.py.py
# ImakerLab-Website-Flask
from flask import Blueprint

tutor_route = Blueprint(__name__, 'tutor_route')
from .login import *
from .register import *
from .list import *
