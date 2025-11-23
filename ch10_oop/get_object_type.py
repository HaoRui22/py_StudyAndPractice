# 获取对象信息
import animals

# 通过 type() 判断对象类型
# 基本类型都可以使用 type() 判断
print(type(123))
print(type("hello"))
print(type(None))

# 指向函数或类的变量，也可以用 type() 判断
print(type(abs))

ani = animals.Animal()
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

result = type(abs) == types.BuiltinFunctionType
print(result)

result = type(fn) == types.BuiltinFunctionType
print(result)

result = type(lambda x: x) == types.LambdaType
print(result)

result = type((x for x in range(10))) == types.GeneratorType
print(result)


# 对于 class 的继承关系，使用 type() 并不方便。可以使用 isinstance() 函数:

a = animals.Animal()
d = animals.Dog()
s = animals.Schnauzer()

print(isinstance(s, animals.Schnauzer))
print(isinstance(s, animals.Dog))
print(isinstance(s, animals.Animal))
print(isinstance(d, animals.Animal))
print(isinstance(d, animals.Schnauzer)) # False

# 能用 type() 判断的基本类型也可以用 isinstance() 判断：
print(isinstance('a', str))
print(isinstance(123, int))

print(type(b'a'))
print(isinstance(b'a', bytes))

# 使用 dir() 函数获取对象的所有属性和方法
print(dir(animals.Animal))
print(dir(animals.Schnauzer))
print(dir(animals.Dog))

class MySZ(animals.Schnauzer):
    def __len__(self):
        return 100

print(len(MySZ()))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
result = len('ABC') == 'ABC'.__len__()
print(result)

# dir() 配合 getattr() setattr() hasattr() 可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9 # 硬编码，因此不需要在 __init__() 内传入参数
    
    def power(self):
        return self.x * self.x
    
myobj = MyObject()

print(hasattr(myobj, 'x'))
print(myobj.x)
print(hasattr(myobj, 'y'))
setattr(myobj, 'y', 10)
print(hasattr(myobj, 'y'))
print(myobj.y)
print(getattr(myobj, 'y'))

print(getattr(myobj, 'z', 404)) # 传入 defau 参数 404，否则属性不存在的话会抛出报错AttributeError

# 也可以获得对象的方法
print(hasattr(myobj, 'power'))
print(getattr(myobj, 'power'))

fn = getattr(myobj, 'power') # 获取 myobj 的属性并赋值到变量 fn
print(fn)
print(fn())

# 不知道对象信息的情况下再去获取信息
# 如果能
sum = myobj.x + myobj.y
# 就不要
sum = getattr(myobj, 'x') + getattr(myobj, 'y')