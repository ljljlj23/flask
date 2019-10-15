from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))    # 当前文件，项目所在的根目录
# # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASE_DIR,'test.db')    # 连接sqlite3
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:181818@localhost/flask'    # 连接mysql
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    # 请求结束之后自动提交
# app.config['SQLALCHEMY_RTACK_MODIFICATIONS'] = True    # 跟踪修改，flask 1.x之后增加的配置项
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['DEBUG'] = True

# app.config.from_pyfile('settings.py')    # 使用python文件做配置
app.config.from_object('settings.Config')    # 使用类对象
# app.config.from_envvar()    # 环境变量中加载
# app.config.from_json()    # 从json串中加载
# app.config.from_mapping()    # mapping->字典类型

db = SQLAlchemy(app)    # 创建对象，绑定flask项目