def foo():
    print('foo')

def bar():
    print('bar')

# __name__ 是 Python 中一个隐含的变量，它代表了模块的名字
# 只有被 Python 解释器直接执行的模块的名字才是 __main__
if __name__ == "__main__":
    print('call foo()')
    foo()
    print('call bar()')
    bar()