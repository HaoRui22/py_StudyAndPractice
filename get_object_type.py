# 获取对象信息
from animals import Animal

# 通过 type() 判断对象类型
# 基本类型都可以使用 type() 判断
print(type(123))
print(type("hello"))
print(type(None))

# 指向函数或类的变量，也可以用 type() 判断
print(type(abs))

ani = Animal()
print(type(ani))

print(type(type(99)))

# type()函数返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
result = type(123) == type(99)
print(result)

result = type(99) == int
print(result)

result = type('abc') == type('123')
print(result)

result = type('abc') == str
print(result)

result = type('abc') == type(123)
print(result) #False

# 判断一个对象是否是函数，使用 types 模块中定义的常量：
import types

def fn():
    pass

result = type(fn) == types.FunctionType
print(result)