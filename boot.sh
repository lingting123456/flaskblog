#!/bin/sh

# 确保目录存在并有正确的权限
mkdir -p instance app/static/uploads/posts app/static/uploads/avatars
# 1: 执行权限
# 2: 写权限 
# 4: 读权限
# 三个数字分别代表所有者、组、其他用户
chmod -R 755 instance app/static/uploads

# 等待数据库就绪
echo "Waiting for database..."

# 初始化数据库
flask db init || true  # 如果已经初始化则跳过
flask db migrate -m "Initial migration" || true  # 生成迁移脚本
flask db upgrade  # 应用迁移

# 自动创建管理员账号
echo "Creating admin account..."
# 使用环境变量创建管理员账号
if [ ! -z "$ADMIN_USERNAME" ] && [ ! -z "$ADMIN_EMAIL" ] && [ ! -z "$ADMIN_PASSWORD" ]; then
    echo "Creating admin account..."
    flask create-admin --username "$ADMIN_USERNAME" --email "$ADMIN_EMAIL" --password "$ADMIN_PASSWORD"

    # 如果AUTO_GENRATE_POSTS为true，则生成测试数据
    if [ "$AUTO_GENRATE_POSTS" = "true" ]; then
        echo "Generating test data..."
        flask init-data
    fi
fi

# 启动应用
echo "Starting Flask application..."
flask run --host=0.0.0.0   # 允许从容器外部访问应用