#!/usr/bin/python3.6
# @Time    : 2021/8/28 14:28
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : list.py
# ImakerLab-Website-Flask
from sqlalchemy import and_, or_
from web.views.tutor import tutor_route, build_doc_path, swag_from
from web.models.User import *
from flask import g
from common.libs.ResponseManage import ResponseManage
from flask import request
import json
from flask import jsonify
from flask_paginate import Pagination, get_page_parameter


@tutor_route.route("/getBaseInfo")
@swag_from(build_doc_path('tutor/getBaseInfo.yml'))
def get_tutor_base_info():
    tutor = g.tutor
    res = {
        'code': '200',
        'message': 'success',
        'user_info': {
            'username': tutor.username,
            'uid': tutor.uid,
            'roleType': tutor.roleType,
            'campus': tutor.campus,
            'group': {
                'group_id': tutor.group_id,
                'group_name': GroupSerializer.check_group_by_id(tutor.group_id)[0].group_name
            }
        },

    }
    return ResponseManage.build_json_response(res)


@tutor_route.route('/list')
@swag_from(build_doc_path('tutor/getBaseInfo.yml'))
def get_tutor_list():
    query = dict(request.values)
    if not query:
        try:
            query = dict(json.loads(request.get_data().decode('utf-8')))
        except Exception as e:
            pass

    page = int(query['page'] if 'page' in query and query['page'] and int(query['page']) > 0 else 1)
    pre_page = int(
        query['pre_page'] if 'pre_page' in query and query['pre_page'] and int(query['pre_page']) > 0 else 10)
    group_name = query['group_name'] if 'group_name' in query else ''

    filters = []

    leader = g.tutor  # 室长账号查询导师
    filters.append(Tutor.campus == leader.campus)  # 选择相同校区的导师

    for key, value in query.items():
        if value and key not in TutorSerializer.ignore_keys:
            filters.append(getattr(Tutor, key) == value)

    if group_name:
        group = GroupSerializer.check_group_by_name(group_name)
        if group.__class__ != Error:
            filters.append(Tutor.group_id == group[0].id)

    tutor_list = [TutorSerializer.serializer(tutor) for tutor in list(Tutor.query.filter(and_(*filters)))]
    total = len(tutor_list)
    pagination = Pagination(tutor_list, page=page, total=total, per_page=pre_page)

    # 对数据进行切片
    tutor_list = tutor_list[(page - 1) * pre_page:(page - 1) * pre_page + pre_page]
    res = {
        'tutor': {
            'tutor_list': tutor_list,
            'pre_page': pre_page,
            'page': page,
            'total_elements': total,
            'total_page': pagination.total_pages,
        },
        'code': '200',
        'message': 'success',
    }
    return ResponseManage.build_json_response(res)


'''
删除导师
@:param:  uid
'''
@tutor_route.route("/delete", methods=["POST"])
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

        tutor = TutorSerializer.get_tutor_by_uid(uid)[0]
        if tutor.__class__ == Error:
            return ResponseManage.build_error_response(tutor)

        db.session.delete(tutor)
        db.session.commit()

        res = {
            'code': '200',
            'message': f'删除导师{tutor.username}成功!'
        }
        return ResponseManage.build_json_response(res)

    except Exception as e:
        error = Error(BaseErrorMessage.Server_Error, str(e))
        print(e, e.__traceback__.tb_lineno)
        return ResponseManage.build_error_response(error)
