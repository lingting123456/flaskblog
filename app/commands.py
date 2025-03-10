import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models.user import User
from app.models.post import Post, Category, Tag
from app.models.comment import Comment
from faker import Faker
import random
import os
from slugify import slugify

fake = Faker('zh_CN')

def init_data():
    """初始化数据（生成slug等）"""
    # 为所有分类生成slug
    for category in Category.query.all():
        if not category.slug:
            category.generate_slug()
    
    # 为所有标签生成slug
    for tag in Tag.query.all():
        if not tag.slug:
            tag.generate_slug()
    
    # 为所有文章生成slug
    for post in Post.query.all():
        if not post.slug:
            post.generate_slug()
    
    db.session.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """初始化数据库"""
    try:
        # 确保instance目录存在
        from flask import current_app
        os.makedirs(current_app.instance_path, exist_ok=True)
        
        # 创建数据库表
        db.create_all()
        
        # 初始化数据
        init_data()
        
        click.echo('数据库初始化完成。')
    except Exception as e:
        click.echo(f'初始化数据库时出错: {e}')

@click.command('create-admin')
@click.option('--username', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@with_appcontext
def create_admin(username, email, password):
    """Create admin user"""
    user = User(
        username=username,
        email=email,
        is_admin=True
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    click.echo('Admin user created successfully.')

@click.command('init-data')
@with_appcontext
def init_data_command():
    """Generate test data"""
    try:
        # 查找管理员用户
        admin = User.query.filter_by(is_admin=True).first()
        if not admin:
            click.echo('错误: 请先创建管理员账户再生成测试数据')
            return
            
        # 创建默认分类
        categories = []
        category_names = ['技术', '生活', '随笔', '读书', '音乐']
        for name in category_names:
            category = Category.query.filter_by(name=name).first()
            if not category:
                category = Category(
                    name=name,
                    author_id=admin.id
                )
                db.session.add(category)
                db.session.flush()
            categories.append(category)
        
        # 创建默认标签
        tags = []
        tag_names = ['Python', 'Flask', 'Web开发', '编程', '数据库', 
                    '前端', '后端', 'Linux', '开源', '人工智能']
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name, author_id=admin.id)
                db.session.add(tag)
                db.session.flush()
            tags.append(tag)
        
        # 生成测试文章
        for i in range(50):
            title = fake.sentence()
            post = Post(
                title=title,
                slug=None,
                summary=fake.text(max_nb_chars=200),
                content='\n\n'.join(fake.paragraphs(nb=5)),
                author=admin,
                category=random.choice(categories),
                is_published=random.choice([True, True, True, False]),
                view_count=random.randint(0, 1000)
            )
            post.tags = random.sample(tags, random.randint(1, 4))
            db.session.add(post)
        
        # 生成测试评论
        posts = Post.query.all()
        for i in range(200):
            post = random.choice(posts)
            comment = Comment(
                content=fake.paragraph(),
                author=admin,
                post=post,
                is_approved=random.choice([True, True, True, False])
            )
            db.session.add(comment)
        
        db.session.commit()
        click.echo('测试数据生成成功！')
        
    except Exception as e:
        db.session.rollback()
        click.echo(f'生成测试数据时出错: {e}')

def init_app(app):
    """注册命令"""
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_admin)
    app.cli.add_command(init_data_command) 