print(abs(-10))
print(abs)

#变量可以指向函数
f = abs
print(f)
#可以通过变量调用指向的函数
print(f(-100))

#高阶函数
def addabs(x, y, f):
    return f(x)+f(y)
x = -9
y = -6
f = abs
print(addabs(x, y, f))