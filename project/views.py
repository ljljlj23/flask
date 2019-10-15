from flask import render_template,request,redirect,session
from main import app
from date import MyDate
from models import *
from settings import STATIC_PATH
import hashlib
import os
import functools

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def loginVaild(func):
    @functools.wraps(func)    # 保留原函数名
    def inner(*args,**kwargs):
        user_id = request.cookies.get('user_id')
        email = request.cookies.get('email')
        session_email = session.get('email')
        if user_id and email and email == session_email:
            user = User.query.filter_by(email=email,id=user_id).first()
            if user:
                return func(*args,**kwargs)
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return inner

@app.route('/index/')
@loginVaild
def index():
    data = UserInfo.query.get(9)
    return render_template('index.html',**locals())

@app.route('/userinfo/',methods=['get','post'])
@loginVaild
def userinfo():
    # 信息
    user = User.query.get(request.cookies.get('user_id'))
    if request.method == 'POST':
        user.name = request.form.get('name')
        age = request.form.get('age')
        if age != 'None':
            user.age = int(age)
        sex = request.form.get('sex')
        if sex == '男':
            user.sex = 1
        elif sex == '女':
            user.sex = 0
        user.identity = request.form.get('identity')
        user.subject = request.form.get('subject')
        user.level = request.form.get('level')
        photo = request.files.get('photo')
        if photo:
            # 将图片保存到本地
            file_name = photo.filename
            photo_path = os.path.join('img', file_name)
            path = os.path.join(STATIC_PATH, photo_path)
            photo.save(path)
            # 将路径保存到数据库中
            user.photo = photo_path
        user.merge()
    # 日历
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
                response = redirect('/index/')
                response.set_cookie('email',email)
                response.set_cookie('user_id',str(user.id))
                session['email']=email
                return response
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

@app.route('/photo/',methods=['get','post'])
def photo():
    if request.method == 'POST':
        user_id = request.form.get('id')
        photo = request.files.get('photo')
        user = User.query.filter_by(id=user_id).first()
        if user:
            # 将图片保存到本地
            file_name = photo.filename
            photo_path = os.path.join('img',file_name)
            path = os.path.join(STATIC_PATH,photo_path)
            photo.save(path)
            # 将路径保存到数据库中
            user.photo = photo_path
            user.save()
    user = User.query.first()
    photo = user.photo
    return render_template('photo.html',**locals())

@app.route('/logout/',methods=['get','post'])
def logout():
    response = redirect('/login/')
    response.delete_cookie('email')
    response.delete_cookie('user_id')
    # print(session.pop('email'))
    del session['email']
    return response

# 接收表单get请求的参数
@app.route('/testget/')
def testget():
    name = request.args.get('name')
    print(name)
    return render_template('testget.html')

@app.route('/leave_list/',methods=['get','post'])
@loginVaild
def leave_list():
    user = User.query.get(request.cookies.get('user_id'))
    if request.method == 'POST':
        flag = 1
        data = request.form
        for one in data.keys():
            if not data[one]:
                flag = 0
        if flag:
            leave = LeaveList()
            leave.request_id = request.cookies.get('user_id')
            leave.request_name = user.name
            leave.request_type = data.get('type')
            leave.request_start = data.get('start')
            leave.request_end = data.get('end')
            leave.request_description = data.get('dec')
            leave.request_phone = data.get('phone')
            leave.request_status = 0
            leave.save()
            return redirect('/leave_all_list/')
        else:
            error = '表中项目均不可为空'
    return render_template('leave_list.html',**locals())

@app.route('/leave_all_list/',methods=['get','post'])
@loginVaild
def leave_all_list():
    user = User.query.get(request.cookies.get('user_id'))
    leave = LeaveList.query.all()
    return render_template('leave_all_list.html',**locals())