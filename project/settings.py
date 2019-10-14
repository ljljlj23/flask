import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))    # 当前文件，项目所在的根目录

class Product():
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 请求结束之后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True  # 跟踪修改，flask 1.x之后增加的配置项
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

# 正式环境配置
class Config(Product):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:181818@localhost/flask'  # 连接mysql

# 测试环境配置
class TestConfig(Product):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'test.db')    # 连接sqlite3