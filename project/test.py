from flask import Flask

app=Flask(__name__)
# app.config['DEBUG']=False
app.config.from_envvar('DEBUG',silent=True)    # 加载了mysettings.py文件

if __name__ == '__main__':
    app.run()