#!/usr/bin/python3.6
# @Time    : 2021/9/2 20:58
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : list.py
# ImakerLab-Website-Flask
import json

from common.libs.ResponseManage import ResponseManage
from web.views.group import group_route
from web.models.User import *
from flask import request
from flask_paginate import Pagination


@group_route.route("/list")
def get_group_list():
    try:
        # 兼容postman 和 axios
        query = dict(request.values)
        if not query:
            try:
                query = dict(json.loads(request.get_data().decode('utf-8')))
            except Exception as e:
                pass

        page = int(query['page'] if 'page' in query and query['page'] and int(query['page']) > 0 else 1)
        pre_page = int(
            query['pre_page'] if 'pre_page' in query and query['pre_page'] and int(query['pre_page']) > 0 else 10)

        filters = []
        for key, value in query.items():
            if value and key not in GroupSerializer.ignore_keys:
                filters.append(getattr(Group, key) == value)

        group_list = [GroupSerializer.serializer(group) for group in list(Group.query.filter(and_(*filters)))]
        total = len(group_list)
        # 分页
        group_list = group_list[(page - 1) * pre_page:(page - 1) * pre_page + pre_page]
        pagination = Pagination(group_list, page=page, total=total, per_page=pre_page)
        res = {
            'group': {
                'tutor_list': group_list,
                'pre_page': pre_page,
                'page': page,
                'total_elements': total,
                'total_page': pagination.total_pages,
            },
            'code': '200',
            'message': 'success',
        }
        return ResponseManage.build_json_response(res)
    except Exception as e:
        error = Error(BaseErrorMessage.Server_Error, str(e))
        return ResponseManage.build_error_response(error)


@group_route.route('/newGroup', methods=['POST'])
def add_group():
    try:
        query = dict(request.values)
        if not query:
            try:
                query = dict(json.loads(request.get_data().decode('utf-8')))
            except Exception as e:
                pass

        group_name = query['group_name'] if 'group_name' in query else ''
        if not group_name:
            error = Error(BaseErrorMessage.Message_Lacking, None)
            return ResponseManage.build_error_response(error)

        # 查重
        group_ = Group.query.filter(Group.group_name == group_name).all()
        print(group_)
        if len(group_) > 0:
            return ResponseManage.build_error_response(Error(BaseErrorMessage.Has_Already_Reg, None))

        group = Group()
        group.group_name = group_name

        db.session.add(group)
        db.session.commit()

        group_info = GroupSerializer.serializer(group)
        if group_info.__class__ == Error:
            return ResponseManage.build_error_response(group_info)

        res = {
            "code": '200',
            'message': f'创建组{group_name}成功',
            'group': GroupSerializer.serializer(group)
        }
        return ResponseManage.build_json_response(res)

    except Exception as e:
        error = Error(BaseErrorMessage.Server_Error, str(e))
        print(e, e.__traceback__.tb_lineno)
        return ResponseManage.build_error_response(error)


@group_route.route('/delete',methods=["POST"])
def delete_group():
    # try:
        query = dict(request.values)
        if not query:
            try:
                query = dict(json.loads(request.get_data().decode('utf-8')))
            except Exception as e:
                pass
        group_id = query['id'] if 'id' in query else ''
        # 非空校验
        if not group_id:
            return ResponseManage.build_error_response(Error(BaseErrorMessage.Message_Lacking, None))

        group = Group.query.filter(Group.id == group_id).all()[0]
        if not group:
            return ResponseManage.build_error_response(Error(BaseErrorMessage.Not_Found_Object, None))

        db.session.delete(group)
        db.session.commit()

        res = {
            'code': '200',
            'message': f'删除组{group.group_name}成功!'
        }
        return ResponseManage.build_json_response(res)

    # except Exception as e:
    #     error = Error(BaseErrorMessage.Server_Error, str(e))
    #     print(e, e.__traceback__.tb_lineno)
    #     return ResponseManage.build_error_response(error)
