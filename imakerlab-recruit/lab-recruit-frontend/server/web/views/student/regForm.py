#!/usr/bin/python3.6
# @Time    : 2021/8/16 22:38
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : regForm.py
# ImakerLab-Website-Flask
import json

from flask import Blueprint
from flask import request
from sqlalchemy import and_, or_
from web.models.User import *
from common.libs.Message.Error import *
from common.libs.Message.Success import *
from common.libs.UserService import *
from common.libs.ResponseManage import *
from web.views.email.email import send_reg_success
from web.views.student import student_route
from flasgger import swag_from
from tools.docsTools import *


@student_route.route("/reg/", methods=["POST"])
@swag_from(build_doc_path('/student/reg.yml'))
def reg_application():
    query = dict(request.values)
    if not query:
        query = dict(json.loads(request.get_data().decode('utf-8')))
    if not UserService.check_not_null(app.config['STUDENT_FIELD'], query):
        return ResponseManage.build_error_response(Error(RegErrorMessage.Message_Lacking, None))

    username = query['username']
    uniLearn = query['uniLearn']
    campus = query['campus']
    group = query['group']

    try:
        res = StudentSerializer.check_has_reg_student(username, uniLearn)
        if res.__class__ == Error:
            return ResponseManage.build_error_response(res)

        group = GroupSerializer.check_group_by_name(group)
        if group.__class__ == Error:
            return ResponseManage.build_error_response(group)
        query['group'] = group[0].id
        group_name = group[0].group_name

        if campus != "泰达校区" and campus != "河西校区":
            return ResponseManage.build_json_response(RegErrorMessage.Campus_Message_Wrong)
        student = StudentSerializer.create_student(query)

        if student.__class__ == Error:
            return ResponseManage.build_error_response(student)

        if student.__class__ != Error:
            # ubuntu 下不明原因报错
            send_reg_success(student, group_name)
            return ResponseManage.build_json_response(BaseSuccessMessage.Reg_Success)

    except Exception as e:
        print("主进程报错", str(e), "行号", e.__traceback__.tb_lineno)
        return ResponseManage.build_error_response(Error(RegErrorMessage.Server_Error, str(e)))
