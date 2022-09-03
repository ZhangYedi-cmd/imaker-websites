#!/usr/bin/python3.6
# @Time    : 2021/8/30 21:33
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : statusManage.py
# ImakerLab-Website-Flask

# 学生的面试管理
import json
from common.libs.ResponseManage import ResponseManage
from web.views.student import student_route
from flask import request
from application import app
from web.models.User import *
from web.views.email.email import *


# 修改面试状态信息
@student_route.route('/changeStatus', methods=['POST'])
def change_student_status():
    try:
        query = dict(request.values)
        if not query:
            query = dict(json.loads(request.get_data().decode('utf-8')))

        # 非空校验
        uid = query['uid'] if 'uid' in query else ''
        status = query['status'] if 'status' in query else ''
        send_status_mail = query['send_mail'] if 'send_mail' in query else ''

        if not uid:
            error = Error('not found uid', None)
            return ResponseManage.build_error_response(error)

        if status not in app.config['STATUS_LIST']:
            error = Error('not found status', None)
            return ResponseManage.build_error_response(error)
        student = StudentSerializer.get_student_by_uid(uid)

        if not student:
            error = Error("not found student object!", None)
            return ResponseManage.build_error_response(error)

        if student.__class__ == Error:
            return ResponseManage.build_error_response(student)

        student.status = status
        student.email_status = '未发送'
        # 发送邮件
        res = {}
        if send_status_mail:
            res = send_status_message(student)
            student.email_status = '已发送'

        db.session.add(student)
        db.session.commit()
        return ResponseManage.build_json_response(res)
    except Exception as e:
        print("邮件错误信息" + str(e))
        error = Error(BaseErrorMessage.Server_Error, str(e))
        return ResponseManage.build_error_response(error)


# 修改用户信息
@student_route.route("/change", methods=["POST"])
def change_student_info():
    query = dict(request.values)
    if not query:
        query = dict(json.loads(request.get_data().decode('utf-8')))

    uid = query['uid'] if 'uid' in query else ''

    if not uid:
        error = Error(BaseErrorMessage.Message_Lacking, None)
        return ResponseManage.build_error_response(error)

    student = StudentSerializer.get_student_by_uid(uid)

    if not student:
        error = Error(BaseErrorMessage.Not_Found_Object, None)
        return ResponseManage.build_error_response(error)

    # 查询数据库出错
    if student.__class__ == Error:
        return ResponseManage.build_error_response(student)

    # 修改信息
    res = StudentSerializer.change_student_info(student, query)
    if res.__class__ == Error:
        return ResponseManage.build_error_response(res)

    return ResponseManage.build_json_response({
        'code': '200',
        'message': "change success"
    })
