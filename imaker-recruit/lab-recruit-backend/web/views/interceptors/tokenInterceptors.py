#!/usr/bin/python3.6
# @Time    : 2021/8/23 23:10
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : tokenInterceptors.py
# ImakerLab-Website-Flask
from hashlib import md5
import re
from common.libs.Message.Error import *
from common.libs.ResponseManage import *
from common.libs.TokenService import TokenService
from common.libs.Message.Error import *
from flask import request
from application import app
from web.models.User import *
from flask import g

'''
token 认证钩子函数
先说一下大体思路吧

   客户端发送请求到服务器, 先使用钩子函数对其状态进判断
   钩子函数判断请求的url是否时要验证的url  
        1. 首次请求/login, 判断用户信息是否正确
              如果正确, 拿到请求头中的ip地址,user-agent,以及用信息进行md5加密, 返回token信息 存入redis数据库中,
              如果不正确 , 返回错误信息
        2. 其他url进行 token 认证 ,从redis中取出token进行认证, 
                 token信息正确, 业务继续
                 token错误 ,业务终止, 
'''
from web.models.User import TutorSerializer


@app.before_request
def token_api():
    # 先对请求的url进行判读
    path = request.url
    ignore_urls = app.config['IGNORE_URLS']
    pattern = re.compile('|'.join(ignore_urls))
    if re.findall(pattern, path):
        print("不进行token认证")
        return None  # 如果return None，请求继续往下执行

    print("token认证~")

    # 校验token信息
    token = request.headers.get("Authorization")
    print(token)
    if not token:
        return ResponseManage.build_error_response(Error(TokenErrorMessage.Not_Found_Token, None))

    if len(token.split('#')) < 3:
        return ResponseManage.build_error_response(Error(TokenErrorMessage.TokenError, None))

    # 验证token是否正确
    uid = token.split("#")[1]

    # 先查询uid对应的用户是否存在
    tutor = TutorSerializer.check_tutor_by_uid(uid)

    if tutor.__class__ == Error:
        # 无当前查询的用户
        return ResponseManage.build_error_response(tutor)

    real_token = TokenService.get_token(tutor)

    if real_token.__class__ == Error:
        return ResponseManage.build_error_response(real_token)

    if not TokenService.get_token(tutor):
        error = Error(TokenErrorMessage.Login_Out_Time, None)
        return ResponseManage.build_error_response(error)

    if token != real_token.decode('utf-8'):
        error = Error(TokenErrorMessage.TokenError, None)
        return ResponseManage.build_error_response(error)

    g.tutor = tutor
    print(token)
    return None
