from flask import render_template,request,redirect
from main import app
from date import MyDate
from models import *
import hashlib

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

@app.route('/index/')
def index():
    data = UserInfo.query.get(9)
    return render_template('index.html',**locals())

@app.route('/userinfo/')
def userinfo():
    obj = MyDate()
    result = obj.get_date()
    n = len(result)
    return render_template('userinfo.html',**locals())

@app.route('/login/',methods=['get','post'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == setPassword(password):
                return redirect('/index/')
            else:
                msg = '密码错误'
        else:
            msg = '该用户不存在，请先注册'
    return render_template('login.html',**locals())

@app.route('/register/',methods=['get','post'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if email and password and password2:
            user = User.query.filter_by(email=email).first()
            # 邮箱已注册
            if user:
                msg = '该邮箱已注册，请登录'
            else:
                if password == password2:
                    user = User(email=email,password=setPassword(password))
                    user.save()
                    msg = '注册成功'
                else:
                    msg = '两次密码不一致，请重新输入'
        else:
            msg = '邮箱及密码不能为空'
    return render_template('register.html',**locals())

@app.route('/perfect/information/',methods=['get','post'])
def perfect_information():
    if request.method == 'POST':
        data = request.files.get('photo')
        print(data)    # <FileStorage: '1.jpg' ('image/jpeg')>
        method = [one for one in dir(data) if not one.startswith('_')]
        print('filename:%s'%data.filename)    # 文件名称
        print('content_length:%s'%data.content_length)    # 文件长度
        print('content_type:%s'%data.content_type)    # 文件类型
        print('headers:%s'%data.headers)    # 请求头部
        print('mimetype:%s'%data.mimetype)    # 内容类型
        print('mimetype_params:%s'%data.mimetype_params)    # 类型的参数
        print('name:'+data.name)    # 字段名称
    return '获取图片'