import functools

def flask_url(func):
    print('我是flask url装饰器')
    def inner(*args,**kwargs):
        print('url')
        func(*args,**kwargs)
    return inner
def loginouter(func):
    print('我是登录装饰器')
    def inner(*args,**kwargs):
        print('验证')
        func()
    return inner

@flask_url    # 2.index = falsk_url(index)
@loginouter    # 1.index = loginouter(index)
def index():
    print('index')

index()
# index = loginouter(index)
# index()