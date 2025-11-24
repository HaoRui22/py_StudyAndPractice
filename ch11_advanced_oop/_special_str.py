# __str__ & __retr__
# 我们先定义一个Student类，打印一个实例：
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Zane'))
# 打印<__main__.SStudent object at 0x000002623D2106E0>

# 如果定义好 __str__() 方法，就可以返回一个好看的字符串：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
print(Student('Zane'))
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

# 但是在 Python 交互环境中，直接输入变量而不用 print，打印出来的实例还是内存地址
# 因为直接显示变量调用的不是 __str__() 而是 __repr__()，__repr__() 是为调试服务的
# 解决办法是再定义一个 __repr__()，也可以偷懒：__repr__ = __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    __repr__ = __str__
