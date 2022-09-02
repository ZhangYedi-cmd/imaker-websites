#!/usr/bin/python3.6
# @Time    : 2021/8/28 12:57
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : docsTools.py
# ImakerLab-Website-Flask
import os


def build_doc_path(filename):
    return os.path.dirname(os.getcwd()) + "/flaskMTV/docs/api/" + filename

