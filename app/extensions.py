from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_ckeditor import CKEditor
from flask_admin import Admin

# 初始化扩展
db = SQLAlchemy()  # 创建数据库实例
migrate = Migrate()  # 创建迁移实例
login_manager = LoginManager()  # 创建登录管理实例
mail = Mail()  # 创建邮件实例
moment = Moment()  # 创建时间实例
ckeditor = CKEditor()  # 创建富文本编辑实例
admin = Admin(name='博客管理系统', template_mode='bootstrap4')  # 创建后台管理实例