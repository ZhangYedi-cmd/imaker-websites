#!/usr/bin/python3.6
# @Time    : 2021/9/2 20:58
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : __init__.py.py
# ImakerLab-Website-Flask
from flask import Blueprint

group_route = Blueprint(__name__, "group_route")
from .list import *
