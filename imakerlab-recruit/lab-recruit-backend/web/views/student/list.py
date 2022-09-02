#!/usr/bin/python3.6
# @Time    : 2021/8/30 20:55
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : list.py
# ImakerLab-Website-Flask

# 学生的查询接口
import json
from flask_paginate import Pagination
from web.views.student import student_route
from web.models.User import *
from flask import request
from common.libs.ResponseManage import ResponseManage
from flask import jsonify


# 不传参默认返回全部数据

@student_route.route("/list")
def get_students_list():
    # try:
    query = dict(request.values)
    if not query:
        try:
            query = dict(json.loads(request.get_data().decode('utf-8')))
        except Exception as e:
            pass
    tutor_uid = query['tutor_uid'] if 'tutor_uid' in query else ''
    username = query['username'] if 'username' in query else ''
    page = int(query['page'] if 'page' in query and query['page'] and int(query['page']) > 0 else 1)
    academy = query['academy'] if 'academy' in query else ''
    group_name = query['group_name'] if 'group_name' in query else ''
    pre_page = int(
        query['pre_page'] if 'pre_page' in query and query['pre_page'] and int(query['pre_page']) > 0 else 5)

    filters = []

    if tutor_uid:  # 查询导师的校区
        tutor = TutorSerializer.get_tutor_by_uid(tutor_uid)

        if tutor.__class__ == Error:
            return ResponseManage.build_error_response(tutor)
        # 校区过滤信息
        filters.append(Student.campus == tutor[0].campus)
        # 如果是leader请求传入则返回全部学生信息,如果是tutor请求,则返回自己组的学生

        if tutor[0].roleType != 'leader':
            # 选择相同的组
            filters.append(Student.group_id == tutor[0].group_id)

        if group_name:
            group_id = GroupSerializer.check_group_by_name(group_name)[0].id
            filters.append(Student.group_id == group_id)

    # username模糊查询
    if username:
        filters.append(Student.username.like("%{}%".format(username)))

    # 学院模糊查询
    if academy:
        filters.append(Student.academy.like("%{}%".format(academy)))

    for key, value in query.items():
        if value and key not in StudentSerializer.ignore_keys:
            filters.append(getattr(Student, key) == value)

    student_list = [StudentSerializer.serializer(student) if student.__class__ != Error else {} for student in
                    list(Student.query.filter(and_(*filters)))]
    total = len(student_list)
    pagination = Pagination(student_list, page=page, total=total, per_page=pre_page)

    # 对数据进行切片
    student_list = student_list[(page - 1) * pre_page:(page - 1) * pre_page + pre_page]
    res = {
        'student': {
            'student_list': student_list,
            'pre_page': pre_page,
            'page': page,
            'total_elements': total,
            'total_page': pagination.total_pages,
        },
        'code': '200',
        'message': 'success',
    }

    return jsonify(res)


# except Exception as e:
#     print(e, e.__traceback__.tb_lineno)
#     return ResponseManage.build_error_response(Error(BaseErrorMessage.Server_Error, str(e)))


@student_route.route('/summary')
def get_student_summary():
    # try:
    query = dict(request.values)
    if not query:
        try:
            query = dict(json.loads(request.get_data().decode('utf-8')))
        except Exception as e:
            pass
    uid = int(query['uid'] if 'uid' in query else '')

    if not uid:
        error = Error('not found uid', None)
        return ResponseManage.build_error_response(error)

    tutor = TutorSerializer.get_tutor_by_uid(uid)[0]

    if tutor.__class__ == Error:
        return ResponseManage.build_error_response(tutor)

    passed_student_count = []
    not_passed_student_count = []
    on_going_student_count = []
    student_list = [StudentSerializer.serializer(student) for student in tutor.student]
    print("____________________________________________")
    print([student['status'] for student in student_list])
    for student in student_list:
        if student['status'] == '通过':
            passed_student_count.append(student)
            continue
        if student['status'] == '不通过':
            not_passed_student_count.append(student)
            continue
        else:
            on_going_student_count.append(student)

    res = {
        'code': '200',
        'message': 'success!',
        'data': {
            'pass_student_count': len(passed_student_count),
            'not_pass_student_count': len(not_passed_student_count),
            'all_student_count': len(student_list),
            'on_going_student_count': len(on_going_student_count)
        }
    }
    return ResponseManage.build_json_response(res)


# except Exception as e:
#     return ResponseManage.build_error_response(Error(BaseErrorMessage.Server_Error, str(e)))


#  删除学生
@student_route.route("/delete", methods=["POST"])
def delete_student():
    try:
        query = dict(request.values)
        if not query:
            try:
                query = dict(json.loads(request.get_data().decode('utf-8')))
            except Exception as e:
                pass
        uid = int(query['uid'] if 'uid' in query else '')

        if not uid:
            error = Error(BaseErrorMessage.Message_Lacking, None)
            return ResponseManage.build_error_response(error)

        student = StudentSerializer.get_student_by_uid(uid)
        if student.__class__ == Error:
            return ResponseManage.build_error_response(student)

        db.session.delete(student)
        db.session.commit()

        res = {
            'code': '200',
            'message': '删除学生成功!'
        }
        return ResponseManage.build_json_response(res)

    except Exception as e:
        error = Error(BaseErrorMessage.Server_Error, str(e))
        return ResponseManage.build_error_response(error)
