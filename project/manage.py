# 项目的管理文件
import sys
from views import *
from models import *

comment = sys.argv

# 启动项目
# 从终端获取输入的参数
if comment[1]=='runserver':
    if len(comment)>2:
        host = comment[2].split(':')[0]
        port = comment[2].split(':')[1]
        app.run(host=host,port=port)
    else:
        app.run()
elif comment[1]=='migrate':
    db.create_all()