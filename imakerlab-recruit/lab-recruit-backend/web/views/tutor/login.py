#!/usr/bin/python3.6
# @Time    : 2021/8/20 22:21
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : login.py
# ImakerLab-Website-Flask
import json

from flask import Blueprint, request
from common.libs.Message.Success import *
from web.models.User import *
from common.libs.TokenService import *
from common.libs.ResponseManage import ResponseManage

from flasgger import swag_from
from tools.docsTools import *


# 登录相关逻辑
from web.views.tutor import tutor_route


@tutor_route.route("/login", methods=["post"])
@swag_from(build_doc_path('tutor/login.yml'))
def login_api():
    # 获取传过来的参数
    query = dict(request.values)
    if not query:
        query = dict(json.loads(request.get_data().decode('utf-8')))

    username = query["username"] if 'username' in query else ''
    password = query["password"] if 'password' in query else ''

    if not username or not password:
        return ResponseManage.build_error_response(Error(BaseErrorMessage.Message_Lacking, None))

    tutor = TutorSerializer.check_tutor_by_name(username)
    if not tutor:
        return ResponseManage.build_error_response(Error(BaseErrorMessage.Not_Found_Object, None))

    # 验证加密密钥
    key = UserService.encrypt_str(password, tutor.salt)
    if key != tutor.password:
        return ResponseManage.build_error_response(Error(LoginErrorMessage.Password_Wrong, None))

    # 将用户信息, 用户类型, 用户id 加密
    token = UserService.gene_auth_code(tutor) + "#" + str(tutor.uid) + "#" + tutor.roleType

    # 设置token信息
    res = TokenService.set_token(token, tutor)
    # TokenService.delete_token(tutor)
    # redis错误
    if res.__class__ == Error:
        return ResponseManage.build_error_response(res)

    # 查询用户的组信息:
    group = GroupSerializer.check_group_by_id(tutor.group_id)[0]
    if group.__class__ == Error:
        return ResponseManage.build_error_response(group)

    res = BaseSuccessMessage.Login_Success
    res['user_info'] = {
        'uid': tutor.uid,
        'username': tutor.username,
        'roleType': tutor.roleType
    }
    res['token'] = token
    # 登录接口不需要返回详细信息
    # user_info = TutorSerializer.serializer(tutor)
    # if user_info.__class__ == Error:
    #     return ResponseManage.build_error_response(user_info)
    #
    # res['user_info'] = user_info
    return ResponseManage.build_json_response(res)
