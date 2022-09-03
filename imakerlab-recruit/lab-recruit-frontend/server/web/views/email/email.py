#!/usr/bin/python3.6
# @Time    : 2021/8/16 21:36
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : email.py
# ImakerLab-Website-Flask
from flask import Blueprint, jsonify
from application import app
from flask_mail import Mail, Message
from common.libs.UserService import UserService
from common.libs.Message.Error import Error
import os

email_route = Blueprint("email_route", __name__)

app.config.update(
    MAIL_SERVER='smtp.163.com',  # 服务器地址
    MAIL_PROT=587,  # 邮件服务器端口
    MAIL_USE_TLS=True,
    MAIL_USERNAME='zhangyedi2021@163.com',  # 发送邮箱
    MAIL_PASSWORD='ORKVRWJGCNVGCGWV',  # 密码
)

mail = Mail(app)

base_path = os.getcwd()
'''
文件读取对象(单例模式)
'''
with open(f'{base_path}/web/templates/h01.html', encoding='utf-8') as f:
    html = f.read()


# class HtmlReader:
#     inner_obj = None
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.inner_obj:
#             obj = object.__new__(cls)
#             cls.inner_obj = obj
#             # 保存字符串模板
#             obj.html = html
#             return obj
#         else:
#             return cls.inner_obj
#
#     def append_html(self, obj):
#         html = self.html
#         return html + obj


@email_route.route("/get_code")
def send_mail():
    try:
        code = UserService.get_email_code()
        msg = Message(
            subject="Imakerlab邮件验证",
            recipients=['178320369@qq.com'],
            sender=app.config.get("MAIL_USERNAME"),
            body="您的验证码为:%s" % code
        )
        mail.send(msg)
        return jsonify({"message": "发送成功!!", 'code': 200})
    except Exception as e:
        return jsonify({"message": "error", 'code': 500})


# CAMLLYUUHFXXBIHW
def send_reg_success(student, group_name):
    try:
        site = ''
        if student.campus == "河西校区":
            site = "河西校区F608"
        if student.campus == "泰达校区":
            site = "泰达校区大学生活动中心120"

        body = f"{student.username}同学(学号:{student.uniLearn})&nbsp; &nbsp;" \
               f"幸而与你在庸常浮生中相拥，天地间共一掷孤勇。" \
               f"恭喜你成功报名安力群大学生创新实验室{group_name}组\n " \
               f"你的导师为: {' , '.join([i.username for i in student.tutor])} \n" \
               f"面试请关注相关群聊通知.\n  <br/>" \
               f"&nbsp; &nbsp;学习的无垠旅途坎坷多磨，我们愿为你扫尽前路的障碍，但未来的巨石终是由你自己推动。认清自己，\n" \
               f"才能不会让有限的知识与无限的鸡汤把你局面于惰愈的牢笼，停滞不前" \
               f"人生百年，吾道不孤，我们期待着你的成长。愿你星河璀璨，未来可期。"

        my_html = html + body

        msg = Message(
            subject="Imakerlab纳新邀请函",
            recipients=[student.email],
            sender=app.config.get("MAIL_USERNAME"),
            html=my_html
        )
        mail.send(msg)
        return {"message": "发送成功!!", 'code': 200}
    except Exception as e:
        print("邮件错误信息" + str(e))
        return Error({"message": "error", 'code': 500}, str(e))


# CAMLLYUUHFXXBIHW
def send_status_message(student):
    try:
        status = student.status

        body = f"Hello，{student.username}同学(学号:{student.uniLearn})：<br/>&nbsp; &nbsp;&nbsp; &nbsp;" \
               f"幸而与你在庸常浮生中相拥，天地间共一掷孤勇。\n" \
               f"恭喜您成功通过天津科技大学安力群创新实验室{status}。" \
               f"<br/>&nbsp; &nbsp;&nbsp; &nbsp;学习的无垠旅途坎坷多磨，" \
               f"我们愿为你扫尽前路的障碍，但未来的巨石终是由你自己推动。认清自己，" \
               f"才能不会让有限的知识与无限的鸡汤把你局囿于惰怠的牢笼，停滞不前。希望你能在接下来的学习中继续提升自我，以热忱之心迎接即将到来的下一轮面试。" \
               f"<br/>&nbsp; &nbsp;&nbsp; &nbsp;人生百年，吾道不孤。再一次恭喜你通过面试，我们期待着你的成长。愿你星河璀璨, 未来可期。<br/>"

        if student.status == '通过':
            status = '全部面试'
            body = f"{student.username}同学(学号:{student.uniLearn})" \
                   f"恭喜你通过了{status},愿你继续努力, 加油!"

        if student.status == '不通过':
            # body = f"{student.username}同学(学号:{student.uniLearn})" \
            #        f"很遗憾, 你未通过创新实验室的考核"
            body = f"""  
        亲爱的{student.username}同学(学号:{student.uniLearn})
        ：<br/>&nbsp; &nbsp;&nbsp; &nbsp;
        首先，感谢报名创新实验室的热情！相信是理想的牵引与对优秀的追求，
        让你选择报名创新实验室。我们同样珍视你的每一份付出，更珍视少年的璀璨时光，
        但由于选择的道路与个人实际情况的不同，非常遗憾你未能通过面试。
        <br/>&nbsp; &nbsp;&nbsp; &nbsp;关山初度，前路由长，
        我们期盼你读完这封信后，能够在短暂的思考之后重新启程，继续在人生的路上披荆斩棘，
        追寻梦想，能一如既往的继续走下去。"""

        my_html = html + body

        msg = Message(
            subject="Imakerlab面试进度通知",
            recipients=[student.email],
            sender=app.config.get("MAIL_USERNAME"),
            html=my_html
        )
        mail.send(msg)
        return {"message": "发送成功!!", 'code': 200}
    except Exception as e:
        print("邮件错误信息" + str(e))
        return Error({"message": "error", 'code': 500}, str(e))
