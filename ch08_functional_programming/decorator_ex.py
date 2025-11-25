# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
from datetime import datetime

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        # 在函数调用时开始计时
        start_time = time.time()
        result = fn(*args, **kw) # 执行原函数
        end_time = time.time()

        # 计算时间
        execut_time = (end_time - start_time) # s
        print(f"{fn.__name__} executed in {execut_time} s")
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print(f)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f"{datetime.now()}, {text}: begin call")
            start_time = time.time()
            result = func(*args, **kw)
            print(f"{datetime.now()}, {text}: end call")
            end_time = time.time()

            execut_time = (end_time - start_time)
            print(f"{text} executed in {execut_time} s")
            return result
        return wrapper
    return decorator

@log('action')
def fast(x, y):
    print("waiting for loading")
    time.sleep(1)
    print("loading")
    time.sleep(2)
    print("running")
    time.sleep(3)
    return x + y

r = fast(11, 22)
print(f"result: {r}")