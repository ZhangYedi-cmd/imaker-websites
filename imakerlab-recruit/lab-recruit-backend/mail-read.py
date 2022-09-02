#!/usr/bin/python3.6
# @Time    : 2021/9/26 17:59
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : mail-read.py
# ImakerLab-Website-Flask
import re


class HtmlReader:
    inner_obj = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.inner_obj:
            obj = object.__new__(cls)
            cls.inner_obj = obj
            with open('web/templates/h01.html') as f:
                html = f.read()
            # 保存字符串模板
            obj.html = html
            return obj
        else:
            return cls.inner_obj

    def append_html(self, obj):
        html = self.html + obj
        return html



