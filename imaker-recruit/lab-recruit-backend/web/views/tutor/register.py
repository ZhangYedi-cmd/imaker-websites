#!/usr/bin/python3.6
# @Time    : 2021/8/20 22:21
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : register.py
# ImakerLab-Website-Flask
import json

from flask import Blueprint
from flask import request

from common.libs.Message.Error import BaseErrorMessage, TutorRegErrorMessage
from common.libs.Message.Success import BaseSuccessMessage
from web.models.User import *
from application import app
from web.views.tutor import tutor_route
from flasgger import swag_from
from tools.docsTools import *
from common.libs.ResponseManage import ResponseManage


@tutor_route.route("/register", methods=['POST'])
@swag_from(build_doc_path('tutor/register.yml'))
def register():
    # 获取传过来的参数
    query = dict(request.values)
    # axios 参数获取
    if not query:
        query = dict(json.loads(request.get_data().decode('utf-8')))

    # 对传过来的字段进行非空校验
    res = UserService.check_not_null(app.config['TUTOR_FIELD'], query)
    if not res:
        error = Error(BaseErrorMessage.Message_Lacking, None)
        return ResponseManage.build_error_response(error)

    # 先检查是否已经注册?
    tutor = TutorSerializer.check_tutor_by_name(query['username'])

    if tutor.__class__ == Error:
        # 返回数据库报错信息
        return ResponseManage.build_error_response(tutor)

    # 已经注册, 返回
    if tutor:
        error = Error(TutorRegErrorMessage.Tutor_Has_Already_Reg, None)
        return ResponseManage.build_error_response(error)

    # 校验组名
    group_name = query['group']
    group = GroupSerializer.check_group_by_name(group_name)

    if group.__class__ == Error:
        return ResponseManage.build_error_response(group)
    query['group'] = group[0].id

    # 校验校区名
    campus_name = query['campus']
    if campus_name != "泰达校区" and campus_name != "河西校区":
        error = Error(RegErrorMessage.Campus_Message_Wrong, None)
        return ResponseManage.build_error_response(error)

    # 校验完成 ==> 存储导师信息
    res = TutorSerializer.ab_serializer(query)

    if res.__class__ == Error:
        return res

    return ResponseManage.build_json_response(BaseSuccessMessage.Tutor_Register_Success)
