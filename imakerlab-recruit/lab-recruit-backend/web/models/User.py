#!/usr/bin/python3.6
# @Time    : 2021/8/16 18:05
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : User.py
# ImakerLab-Website-Flask


from sqlalchemy import and_, or_
from common.libs.UserService import UserService
from application import db
from common.libs.Message.Error import Error, RegErrorMessage, BaseErrorMessage

association_table = db.Table('association', db.metadata,
                             db.Column('student_id', db.Integer, db.ForeignKey('student.uid')),
                             db.Column('tutor_id', db.Integer, db.ForeignKey('tutor.uid')))


class Tutor(db.Model):
    """
     导师类
     """
    tablename = "Tutor"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(100))
    salt = db.Column(db.String(100))  # 加密密钥
    email = db.Column(db.String(100))  # 邮箱
    campus = db.Column(db.Enum("河西校区", "泰达校区"), server_default="泰达校区")
    student = db.relationship("Student", back_populates="tutor", secondary=association_table)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))  # 组
    qq = db.Column(db.String(20))
    roleType = db.Column(db.Enum("tutor", "leader"), server_default="tutor")  # 用户类型
    status = db.Column(db.Enum("已审核", "未审核"), server_default="未审核")  # 导师登录时验证用户类型 + 状态否则无法登录


class TutorSerializer(Tutor):
    # 导师对象调用序列化方法, 返回Json
    # 查询时忽略的key
    ignore_keys = ['group_name', 'page', 'pre_page']

    @staticmethod
    def get_tutor_by_uid(uid):
        try:
            tutor = Tutor.query.filter(Tutor.uid == uid)
            if len(list(tutor)) == 0:
                return Error(BaseErrorMessage.Not_Found_Object, None)
            print(tutor)
            return tutor
        except Exception as e:
            return Error(BaseErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def serializer(self):
        # 查询用户的组信息:
        print(self)
        group = GroupSerializer.check_group_by_id(self.group_id)[0]
        if group.__class__ == Error:
            return group

        return {
            'uid': self.uid,
            'username': self.username,
            'email': self.email,
            'roleType': self.roleType,
            'group': {
                'group_id': self.group_id,
                'group_name': group.group_name
            },
            'student': [{
                'username': student.username,
                'uniLearn': student.uniLearn,
                'email': student.email,
                'interview_time': student.interview_time,
                'status': student.status,
                'campus': student.campus,
                'tel': student.tel,
                'introduce': student.introduce,
                'major': student.major,
                'academy': student.academy,
            } for student in self.student],
        }

    # 反序列化
    @staticmethod
    def ab_serializer(tutor_info):
        try:
            # 对用户密码md5加密
            # 获取一个随机码
            salt = UserService.get_random_salt()
            user_password = tutor_info['password']
            # 加密后新密码
            secret_password = UserService.encrypt_str(user_password, salt)

            # 存储用户信息
            tutor = Tutor()
            tutor.salt = salt
            tutor.username = tutor_info['username']
            tutor.password = secret_password
            tutor.email = tutor_info['email']
            tutor.group_id = tutor_info['group']
            tutor.qq = tutor_info['qq']
            tutor.campus = tutor_info['campus']
            db.session.add(tutor)
            db.session.commit()
            return tutor
        except Exception as e:
            return Error(BaseErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def check_tutor_by_name(username):
        try:
            tutor = Tutor.query.filter(Tutor.username == username).first()
            if tutor:
                return tutor
            else:
                return False
        except Exception as e:
            print(str(e))
            return Error(BaseErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def check_tutor_by_uid(uid):
        try:
            tutor = Tutor.query.filter(Tutor.uid == uid).first()
            # 如果没查到, 就返回
            if not tutor:
                return Error(BaseErrorMessage.Not_Found_Object, None)
            return tutor
        except Exception as e:
            return Error(BaseErrorMessage.DataBase_Error, str(e))

    #  选择组和校区相同的导师
    @staticmethod
    def check_tutor_in_same_campus(campus, group):
        try:
            tutor_list = Tutor.query.filter(and_(Tutor.group_id == group, Tutor.campus == campus)).all()
            return tutor_list
        except Exception as e:
            print("查询同小区导师报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(BaseErrorMessage.DataBase_Error, str(e))


class Student(db.Model):
    """
    学生类
    """
    tablename = "student"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    uniLearn = db.Column(db.String(10))  # 学号
    email = db.Column(db.String(100))  # 邮箱
    interview_time = db.Column(db.DATE)
    status = db.Column(db.Enum("第一轮面试", "第二轮面试", "第三轮面试", "通过", "不通过", "未审核"), server_default="未审核")
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    campus = db.Column(db.Enum("河西校区", "泰达校区"), server_default="泰达校区")
    tel = db.Column(db.String(12))
    introduce = db.Column(db.String(1000))
    # 导师和学生多对多关系
    tutor = db.relationship("Tutor", secondary=association_table, back_populates="student")
    major = db.Column(db.String(100))  # 专业
    academy = db.Column(db.String(100))  # 学院
    annotation = db.Column(db.String(10000))  # 注释
    grade = db.Column(db.String(10000))
    email_status = db.Column(db.Enum("已发送", "未发送"), server_default="未发送")
    rate = db.Column(db.Integer, default=0)


class StudentSerializer(Student):
    # 不支持更改的字段
    ignore_keys = ['group_name', 'page', 'pre_page', 'uid', 'tutor_list', 'tutor_uid', 'username', 'academy']

    @staticmethod
    def change_student_info(student, query):
        try:
            # 要修改的字段
            for key, value in query.items():
                if value and key not in StudentSerializer.ignore_keys:
                    setattr(student, key, value)
            if 'group_name' in query:
                student.group_id = GroupSerializer.check_group_by_name(query['group_name'])[0].id
                # 如果要更改组 也要更改导师
                tutor_list = TutorSerializer.check_tutor_in_same_campus(student.campus, student.group_id)
                student.tutor = tutor_list
            db.session.add(student)
            db.session.commit()

        except Exception as e:
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def get_student_by_uid(uid):
        try:
            return Student.query.filter(Student.uid == int(uid)).first()
        except Exception as e:
            return Error(RegErrorMessage.DataBase_Error, str(e))

    # 序列化学生对象
    @staticmethod
    def serializer(student):
        try:
            print(student.group_id)
            group = GroupSerializer.check_group_by_id(student.group_id)

            if len(group) == 0:
                pass
            if group[0].__class__ == Error:
                return group[0]

            group = group[0]
            return {
                'username': student.username,
                'uid': student.uid,
                'uniLearn': student.uniLearn,
                'email': student.email,
                'interview_time': student.interview_time,
                'status': student.status,
                'group': {
                    'group_id': student.group_id,
                    'group_name': group.group_name
                },
                'campus': student.campus,
                'tel': student.tel,
                'introduce': student.introduce,
                'major': student.major,
                'grade': student.grade,
                'academy': student.academy,
                'annotation': student.annotation,
                'email_status': student.email_status,
                'rate': student.rate,
                'tutor': [
                    # 导师基础信息序列化
                    {
                        'uid': tutor.uid,
                        'username': tutor.username,
                    }
                    for tutor in student.tutor
                ]
            }
        except Exception as e:
            print("序列化学生信息时报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def check_has_reg_student(username, uniLearn):
        try:
            student = Student.query.filter(or_(Student.username == username, Student.uniLearn == uniLearn)).all()
            if len(student) > 0:
                return Error(RegErrorMessage.Has_Already_Reg, None)
            return student
        except Exception as e:
            print("查询用户是否报名时报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def create_student(dic):
        try:
            student = Student()
            student.username = dic['username']
            student.uniLearn = dic['uniLearn']
            student.email = dic['email']
            student.campus = dic['campus']
            # student.interview_time = UserService.get_time(dic['interview_time'])
            # postman测试不传递UTC时间格式,先注释掉
            # student.interview_time = dic['interview_time']
            student.group_id = dic['group']
            #  选择校区相同的导师团
            tutor_list = TutorSerializer.check_tutor_in_same_campus(student.campus, student.group_id)
            student.tutor = tutor_list
            student.tel = dic['tel']
            student.grade = "20" + dic['uniLearn'][:2]
            student.introduce = dic['introduce']
            student.academy = dic['academy']
            student.major = dic['major']
            db.session.add(student)
            db.session.commit()
            return student
        except Exception as e:
            print("创建student时报错!", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))


class Group(db.Model):
    """
    组别类
    """
    tablename = "Group"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(200))
    student_id = db.relationship("Student", backref="group", uselist=False)


class GroupSerializer(Group):
    ignore_keys = ['page', 'pre_page']

    @staticmethod
    def serializer(group):
        try:
            return {
                'group_name': group.group_name,
                'id': group.id,
            }
        except Exception as e:
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def check_group_by_id(group_id):
        try:
            group = Group.query.filter(Group.id == group_id).all()
            if len(group) == 0:
                return Error(RegErrorMessage.Not_Found_Group, None)
            return group
        except Exception as e:
            print("查询组是否存在时报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def check_group_by_name(group_name):
        try:
            print(group_name)
            group = Group.query.filter(Group.group_name == group_name).all()
            if len(group) == 0:
                return Error(RegErrorMessage.Not_Found_Group, None)
            return group
        except Exception as e:
            print("查询组是否存在时报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))

    @staticmethod
    def create_group(name):
        try:
            group_ = Group()
            group_.group_name = name
            db.session.add(group_)
            db.session.commit()
            return group_
        except Exception as e:
            print("创建组时报错", str(e), "行号", e.__traceback__.tb_lineno)
            return Error(RegErrorMessage.DataBase_Error, str(e))
