def test(**kwargs):
    print(kwargs)

def newfunc(**kwargs):
    test(**kwargs)

newfunc(name='zhangsan',age=90)