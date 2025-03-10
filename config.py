import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # 基本配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shsuagdfslhzyigdfpowjqposhxcnn_dsazzsaDSAxzjsa'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE', 10))
    
    # 邮件配置 - 默认使用QQ邮箱配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # 必须在环境变量中设置
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 必须在环境变量中设置
    
    # 上传文件配置
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    
    # 安全配置
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p')