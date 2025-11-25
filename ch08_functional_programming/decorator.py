from datetime import datetime

def now():
    print(datetime.now())

f = now
f()
# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字：
print(f"调用now.__name__：{now.__name__}")
print(f"调用f.__name__：{f.__name__}")

# 日志函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 装饰器：在代码运行期间动态增加功能
@log # now = log(now)  log() is a decorator
def now():
    print(datetime.now())

now()

# 如果 decorator 本身需要传入参数，则编写一个返回 decorator 的高阶函数：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(f"Time: {datetime.now()} {text}: {func.__name__}")
            return func(*args, **kw)
        return wrapper
    return decorator

@log('Execute') # now = log('execut')(now)
def run():
    print("running...")

run()

# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print(f"调用 run.__name__: {run.__name__}")

# 因为返回的那个wrapper()函数名字就是'wrapper'
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(f"Time: {datetime.now()} Called: {func.__name__}")
        return func(*args, **kw)
    return wrapper

@log
def run():
    print("running...")

run()

print(f"调用 run.__name__: {run.__name__}")

# 针对带参数的 decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wraaper(*args, **kw):
            print(f"Time: {datetime.now()} {text}: {func.__name__}")
            return func(*args, **kw)
        return wraaper
    return decorator

@log('Actions')
def run():
    print("running...")

run()

# 练习题文件：decorator_ex.py