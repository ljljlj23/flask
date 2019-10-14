from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 学习sqlalchemy
# 连接数据库
# app.config：类字典
print(__file__)    # E:/第三阶段/FlaskDemo/project/ORMtest.py
print(os.path.dirname(__file__))    # E:/第三阶段/FlaskDemo/project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))    # 当前文件，项目所在的根目录
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASE_DIR,'test.db')    # 连接sqlite3
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:181818@localhost/flask'    # 连接mysql
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    # 请求结束之后自动提交
app.config['SQLALCHEMY_RTACK_MODIFICATIONS'] = True    # 跟踪修改，flask 1.x之后增加的配置项
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)    # 创建对象，绑定flask项目
# 创建模型
from datetime import datetime

class BascModel(db.Model):
    __abstract__ = True    # 声明当前类为抽象类，会被继承调用，不会被创建
    id = db.Column(db.Integer,primary_key=True)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def merge(self):
        db.session.merge(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class UserInfo(BascModel):
    __tablename__ = 'userinfo'
    # id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer,default=1)
    time = db.Column(db.DATETIME,default=datetime.now())

class User(BascModel):
    __tablename__='user'
    # id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    phone = db.Column(db.String(11))

# 利用基类的方法操作数据库
# 增加数据
userinfo = UserInfo(name='wo',age=99)
userinfo.save()
# 修改数据
userinfo = UserInfo.query.get(8)
userinfo.name='wowowo'
userinfo.merge()
# 删除数据
userinfo = UserInfo.query.get(8)
userinfo.delete()

# 数据迁移
db.create_all()    # 同步表结构

'''
增加数据
'''
# 单条增加
# userinfo = UserInfo(name='zhangsan',age=19)
# db.session.add(userinfo)
# db.session.commit()
# 多条增加
# 1
# db.session.add_all([
#     UserInfo(name='lisi',age=23),
#     UserInfo(name='lisi',age=23),
#     UserInfo(name='lisi',age=23),
#     UserInfo(name='lisi',age=23),
#     UserInfo(name='lisi',age=23),
# ])
# db.session.commit()
# 2
# userinfo1 = UserInfo(name='hhh',age=90)
# userinfo2 = UserInfo(name='hhh',age=90)
# userinfo3 = UserInfo(name='hhh',age=90)
# db.session.add_all([userinfo1,userinfo2,userinfo3])
# db.session.commit()

'''
查询数据
'''
# all()
# data = UserInfo.query.all()
# print(data)
# for one in data:
#     print(one.name)
# get()
# data = UserInfo.query.get(10)
# print(data.name)
# filter()
# data = UserInfo.query.filter(UserInfo.name=='lisi').all()
# print(data)
# filter_by()
# data = UserInfo.query.filter_by(name='lisi').all()
# print(data)
# first()
# data = UserInfo.query.filter(UserInfo.name=='lisi').first()
# print(data)
# order_by()
# data = UserInfo.query.order_by(UserInfo.id).all()    # 按照id进行升序
# print(data)
# data = UserInfo.query.order_by(UserInfo.id.desc()).all()    # 按照id进行降序
# print(data)
# data = UserInfo.query.order_by('id').all()    # 按照id进行升序
# print(data)
# data = UserInfo.query.order_by(db.desc('id')).all()    # 按照id进行降序
# print(data)
# 分页
# data = UserInfo.query.limit(2).all()    # 取2条数据
# print(data)
# data = UserInfo.query.offset(2).limit(2).all()    # 跳过前两条，取2条数据
# print(data)

'''
修改数据
'''
# data = UserInfo.query.filter(UserInfo.id==1).first()
# data.name = 'ooo'
# db.session.merge(data)
# db.session.commit()

'''
删除数据
'''
# delete()
# 1
# data = UserInfo.query.filter().first()
# print(data.id)
# db.session.delete(data)
# db.session.commit()
# 2
# UserInfo.query.filter(UserInfo.id==2).delete()
# db.session.commit()

@app.route('/')
def index():
    return 'ORMtest'
