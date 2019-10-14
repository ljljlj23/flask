from datetime import datetime
from main import db

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
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    identity = db.Column(db.String(32))
    subject = db.Column(db.String(32))
    level = db.Column(db.String(64))
    photo = db.Column(db.String(64))