#!/usr/bin/python3.6
# @Time    : 2021/9/25 15:57
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : __init__.py
# ImakerLab-Website-Flask

from flask import Blueprint

file_route = Blueprint(__name__, "file_route")
from .StudentInfo import *
