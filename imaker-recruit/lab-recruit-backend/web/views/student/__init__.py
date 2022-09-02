#!/usr/bin/python3.6
# @Time    : 2021/8/28 10:44
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : __init__.py
# ImakerLab-Website-Flask

from flask import Blueprint

student_route = Blueprint(__name__, 'student_route')
from .regForm import *
from .list import *
from .statusManage import *
from .annotationManage import *