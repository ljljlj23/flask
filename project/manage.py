# 项目的管理文件
import sys
from views import *
from models import *
from flask_script import Manager
# 自带shell和runserver方法

# 将flask应用交给Manager管理
manager = Manager(app)

@manager.command
def migrate():
    db.create_all()

if __name__ == '__main__':
    manager.run()    # runserver方法

# comment = sys.argv
# 启动项目
# 从终端获取输入的参数
# if comment[1]=='runserver':
#     if len(comment)>2:
#         host = comment[2].split(':')[0]
#         port = comment[2].split(':')[1]
#         app.run(host=host,port=port)
#     else:
#         app.run()
# elif comment[1]=='migrate':
#     db.create_all()