# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？
# 在Python中，答案是肯定的。

# 任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"My name is {self.name}")

# 调用方式如下
s = Student('Zane')
s() # self 参数不要传入
s = Student('Avery')
s()