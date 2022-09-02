from web.views.index import route_index
from web.views.static import static_route
from web.views.interceptors.tokenInterceptors import *
from web.views.tutor import tutor_route
from web.views.student import student_route
from web.views.email import email_route
from web.views.group import group_route

app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(static_route, url_prefix="/static")

# 学生相关接口
app.register_blueprint(email_route, url_prefix="/student/email")
app.register_blueprint(student_route, url_prefix="/student")

# 导师相关接口
app.register_blueprint(tutor_route, url_prefix="/tutor")

# 组相关接口
app.register_blueprint(group_route, url_prefix="/group")
