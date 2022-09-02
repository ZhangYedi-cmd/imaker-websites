#!/usr/bin/python3.6
# @Time    : 2021/10/19 12:11
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : 自动发送邮件助手.py
import requests
import json


class Spider:
    def __init__(self):
        # 服务器地址
        self.baseUrl = 'http://49.232.14.242/'

        self.headers = {
            # token
            "Authorization": "b6206c24345082b865d84f8809271400#5#leader"
        }


class ListSpider(Spider):
    def __init__(self, username, status, group_name, page):
        super(ListSpider, self).__init__()
        self.listQuery = {
            "page": page,  # 分页
            "tutor_uid": 5,
            "username": username,
            "pre_page": 10,
            "status": status,  # 状态
            "group_name": group_name
        }

        self.listUrl = self.baseUrl + f"/student/list?page={self.listQuery['page']}&" \
                                      f"tutor_uid={self.listQuery['tutor_uid']}&" \
                                      f"pre_page=10&status={self.listQuery['status']}" \
                                      f"&username={self.listQuery['username']}"

        self.student_list = []
        self.all_page = ''

    def get_student_list(self):
        res = requests.get(self.listUrl, headers=self.headers)
        data = json.loads(res.text)
        self.student_list = data['student']['student_list']
        self.all_page = int(data['student']['total_page'])
        return self.student_list


# 状态修改(发送邮件)
class EmailSpider(Spider):
    def __init__(self, student):
        super(EmailSpider, self).__init__()

        # 传入学生对象
        self.student = student

        self.emailUrl = self.baseUrl + "/student/changeStatus"

        # 发送邮件参数
        self.student['send_mail'] = True

        self.student['email_status'] = "已发送"

    def send_email(self):
        with open("emailLog.txt", 'a', encoding="utf-8 ") as f:

            try:
                # res = json.loads(requests.post(self.emailUrl, data=self.student, headers=self.headers).text)
                # print(res)
                # if res['code'] == '200':
                print("-" * 50)
                print("[INFO] %s  %s %s========> 已经发送邮件通知" % (
                    self.student['uniLearn'], self.student['username'], self.student['email']))

                # f.write("[INFO] %s  %s %s %s 状态========> 已经发送邮件通知\n" % (
                #     self.student['uniLearn'], self.student['username'], self.student['email'],
                #         self.student['status']))
                # else:
                #     print("%s 发送邮件失败" % self.student['username'])
                #     f.write("[INFO] %s  %s %s========> 发送邮件失败\n" % (
                #         self.student['uniLearn'], self.student['username'], self.student['email']))

            except Exception as e:
                print("[ERROR] %s  %s %s========> 发送邮件失败" % (
                    self.student['uniLearn'], self.student['username'], self.student['email']))


# 日志管理对象
class LogManage:
    def __init__(self):
        pass


def get_input_query():
    print("注意事项:  \n"
          "发送邮件前必须去后台修改状态, 例如:通过第一轮面试则修改状态为第一轮面试."
          " \n 姓名可以不填, 自动筛选出指定条件学生")
    username = input("请输入学生姓名>>>")
    status = input("请输入学生状态>>>")
    group_name = input("请输入组名称>>>")

    sp = ListSpider(username, status, group_name, "")
    sp.get_student_list()
    all_page = sp.all_page

    for page in range(int(all_page) + 1):
        spider = ListSpider(username, status, group_name, page)
        spider.get_student_list()
        for student in spider.student_list:
            es = EmailSpider(student)
            es.send_email()


while True:
    print("+++++++++++++++欢迎使用imaker(河西(泰达请修改token信息))自动发送邮件助手+++++++++++")
    menu = {
        "1": {"name": "批量发送邮件选项", "func": get_input_query},
        "2": {"name": "退出", "func": exit}
    }

    for i in menu:
        print(i, menu[i]['name'])

    change = input("输入序号>>>")

    if change not in menu:
        print("输入正确的序号, 憨批")
        continue
    if change == '2':
        print("作者:ZhangYd -- Tust \n Bye ")

    menu[change]['func']()

print("hello world ")
