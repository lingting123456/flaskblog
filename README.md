# Flask Blog

一个基于 Flask 的开源博客系统，支持一键部署。

## 构建镜像

```bash
# 设置网络代理
$ set HTTP_PROXY=http://127.0.0.1:7890
$ set HTTPS_PROXY=http://127.0.0.1:7890
# 构建镜像
$ docker build -t lingting724/flaskblog:latest .
# 检查镜像是否构建成功
$ docker images | grep flaskblog
```

## 发布镜像

```bash
# 登录Docker Hub
$ docker login
# 推送镜像
$ docker push lingting724/flaskblog:latest
```

## 运行容器
```bash
$ docker run -d \
  -p 5000:5000 \
  -e MAIL_USERNAME=your_qq@qq.com \
  -e MAIL_PASSWORD=your_qq_auth_code \
  -e ADMIN_USERNAME=admin \
  -e ADMIN_EMAIL=admin@example.com \
  -e ADMIN_PASSWORD=your_password \
  -e AUTO_GENRATE_POSTS=true \
  -v flaskblog-data:/flaskblog/instance \
  -v flaskblog-uploads:/flaskblog/app/static/uploads \
  lingting724/flaskblog:latest
```


环境变量说明
- 📧 MAIL_USERNAME: QQ邮箱账号
- 🔑 MAIL_PASSWORD: QQ邮箱授权码
- 🧑‍🚀 ADMIN_USERNAME: 管理员用户名
- 📧 ADMIN_EMAIL: 管理员邮箱
- 🔑 ADMIN_PASSWORD: 管理员密码
- 📝 AUTO_GENRATE_POSTS: 是否生成测试数据(true/false)

数据卷说明：
- 📁 flaskblog-data: 存储数据库文件
- 📁 flaskblog-uploads: 存储上传的文件


## 删除数据卷
```bash
# 查看容器
$ docker ps
$ docker stop $(docker ps -aq)
$ docker rm $(docker ps -aq)
$ docker container prune -a -f
# 查看镜像
$ docker images
$ docker image prune -a -f
# 查看数据卷
$ docker volume ls
$ docker volume rm $(docker volume ls -q)
# 清理所有未使用的对象，包括镜像、容器、数据卷
$ docker system prune -a --volumes
```


## 快速开始（普通用户使用）
```bash
# 最简单的运行方式（使用默认配置）
$ docker run -d -p 5000:5000 lingting724/flaskblog:latest 
# 完整配置的运行方式
$ docker run -d \
  -p 5000:5000 \
  -e MAIL_USERNAME=123456789@qq.com \
  -e MAIL_PASSWORD=abcdefghijklmn \
  -e ADMIN_USERNAME=admin \
  -e ADMIN_EMAIL=admin@example.com \
  -e ADMIN_PASSWORD=admin123 \
  -e AUTO_GENRATE_POSTS=true \
  -v flaskblog-data:/flaskblog/instance \
  -v flaskblog-uploads:/flaskblog/app/static/uploads \
  lingting724/flaskblog:latest
```