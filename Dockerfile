# 使用官方 Python 3.9 作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /flaskblog

# 复制 requirements.txt 并安装依赖
COPY requirements.txt /flaskblog/
RUN pip install -r requirements.txt

# 复制项目文件到工作目录
COPY ./ /flaskblog/

# 设置默认环境变量
ENV FLASK_APP=run.py \
    FLASK_ENV=production \
    MAIL_SERVER=smtp.qq.com \
    MAIL_PORT=587 \
    MAIL_USE_TLS=true \
    MAIL_USERNAME='' \
    MAIL_PASSWORD='' \
    ADMIN_USERNAME='' \
    ADMIN_EMAIL='' \
    ADMIN_PASSWORD='' \
    AUTO_GENRATE_POSTS=false

# 设置启动脚本权限
COPY boot.sh /flaskblog/
RUN chmod +x /flaskblog/boot.sh

# 暴露端口
EXPOSE 5000

# 运行启动脚本
CMD ["/flaskblog/boot.sh"]