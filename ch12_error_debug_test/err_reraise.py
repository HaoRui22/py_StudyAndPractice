# 最后，我们来看另一种错误处理的方式：
'''
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError(f"invalid value: {s}")
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print("ValueError!")
        raise

bar()
'''
# 在 bar() 函数中，捕获了错误，再通过 raise 语句抛出错误

# 捕获错误目的是记录，方便后续追踪。但由于当前函数不知道该怎么处理这个错误所以最恰当的方式是继续上抛，让顶层调用者处理。

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。