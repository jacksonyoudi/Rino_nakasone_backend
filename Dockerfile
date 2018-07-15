# 底包镜像
FROM python:3.6.2
MAINTAINER youdi "liangchangyoujackosn@gmail.com"
# 项目位置
RUN mkdir -p /var/www/project
WORKDIR /var/www/project

# 安装依赖
ADD requirements.txt /var/www/project/
RUN pip install -U pip && pip install -r requirements.txt
ADD . /var/www/project