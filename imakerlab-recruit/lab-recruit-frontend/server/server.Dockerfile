FROM python:3.8

COPY ../server/environments.txt .


RUN pip install -r environments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ../server .

#RUN python runProject.py

CMD ["uwsgi","--ini","uwsgi.ini"]
#
EXPOSE 8080
