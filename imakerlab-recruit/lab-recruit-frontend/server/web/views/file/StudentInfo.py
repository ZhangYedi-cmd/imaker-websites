#!/usr/bin/python3.6
# @Time    : 2021/9/25 15:57
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : StudentInfo.py
# ImakerLab-Website-Flask
from web.models.User import *
from web.views.file import file_route
from flask import request, g
import json


@file_route.route('/download/studentInfo')
def download_student_info():
    query = dict(request.values)
    if not query:
        try:
            query = dict(json.loads(request.get_data().decode('utf-8')))
        except Exception as e:
            pass
    group_name = query['group_name'] if 'group_name' in query else ''

    filters = []
    tutor = g.tutor

    # 选择本校区实验室的
    filters.append(Student.campus == tutor.campus)

    # 如果传过来要导入的组 ==> 组筛选
    if group_name:
        group_id = GroupSerializer.check_group_by_name(group_name)[0].id
        filters.append(Student.group_id == group_id)

    student_list = [StudentSerializer.serializer(student) for student in list(Student.query.filter(and_(*filters)))]
