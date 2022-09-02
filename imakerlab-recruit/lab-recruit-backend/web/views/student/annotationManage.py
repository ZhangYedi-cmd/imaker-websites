#!/usr/bin/python3.6
# @Time    : 2021/9/4 19:01
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : annotationManage.py
# ImakerLab-Website-Flask

import json
from common.libs.ResponseManage import ResponseManage
from web.views.student import student_route
from flask import request
from application import app
from web.models.User import *
from web.views.email.email import *


# 面试时添加注释

@student_route.route("/annotation", methods=['POST'])
def annotation():
    try:
        query = dict(request.values)
        if not query:
            try:
                query = dict(json.loads(request.get_data().decode('utf-8')))
            except Exception as e:
                pass

        uid = query['uid'] if 'uid' in query else ''
        user_annotation = query['annotation'] if 'annotation' in query else ''
        rate = query['rate'] if 'rate' in query else ''
        if not uid:
            error = Error(BaseErrorMessage.Message_Lacking, None)
            return ResponseManage.build_error_response(error)

        student = StudentSerializer.get_student_by_uid(uid)
        if student.__class__ == Error:
            return ResponseManage.build_error_response(student)

        student.annotation = user_annotation
        student.rate = rate
        db.session.add(student)
        db.session.commit()

        res = {
            'code': '200',
            'message': '保存注释成功!'
        }
        return ResponseManage.build_json_response(res)
    except Exception as e:
        error = Error(BaseErrorMessage.Server_Error, str(e))
        return ResponseManage.build_error_response(error)
