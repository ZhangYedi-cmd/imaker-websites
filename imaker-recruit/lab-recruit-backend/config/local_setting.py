# -*- coding: utf-8 -*-
# 是否开启debug模式
DEBUG = True

# sqlalchemy ==> mysql
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/imaker'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8"

# redis 相关配置
REDIS_PORT = 6379
REDIS_HOST = "127.0.0.1"
REDIS_DATABASE_INDEX = 0

# 忽略token的url
IGNORE_URLS = ['/login', '/student', '/register', '/flasgger_static', '/apidocs', '/apispec_1.json', '/group/list',
               '/group/newGroup',
               '/index', '/static', '/favicon.ico']
