from flask import Flask

# 实例化app实例
app = Flask(__name__)

# 路由
@app.route('/')
# 视图
def hello():
    return 'hello world'    # 返回值

from flask import redirect,render_template
@app.route('/index/')
def index():
    name = 'hahaha'
    age = 99
    mydict = {'math':100,'yuwen':80}
    return render_template('index.html',**locals())

@app.route('/person/<username>/<int:age>')
def person(username,age):
    return '我的名字是%s，年龄%s'%(username,age)

@app.route('/baidu/<path:url>/')
def baidu(url):
    return url

@app.route('/text/<uuid:id>/')
def text(id):
    return 'text'

from flask import request
@app.route('/reqdemo/',methods=['get','post'])
def reqdemo():
    # data = request.args
    # print(data)
    # print(request.args.get('name'))
    # print(request.args.get('age'))

    data = request.form
    print(data)
    print(request.form.get('name'))
    print(request.form.get('age'))
    return 'reqdemo'

if __name__ == '__main__':
    # 开启debug模式：
    # 1.显示错误内容
    # 2.修改代码之后自动重启
    app.run(host='0.0.0.0',port=8000,debug=True)    # 项目启动