ImakerLab Website -- Flask Service
=====================
##前言
Team: Tust-Imakerlab

Author:   Tust--ZhangYD

Email: 178320369@qq.com  


## 开发文档
#### 前端测试地址
http://39.103.223.8/imaker/home.html
####开发进度
> 8.18 搭建后端基本框架, 设计数据库
>
> 8.19 搭建邮件服务, 纳新功能
>
> 8.21 完成邮箱验证码校验功能, 登录加密(md5), 
>
> 8.23 完善纳新功能, 测试部署到服务器
>
>8.24 redis + token 认证功能, 需要先运行一下redis 
> 

####目前遇到的问题
>1. flask_mail 邮件功能, 在生产环境中不明原因报错, 考虑使用python其他的库去调用smtp服务(8.23)
