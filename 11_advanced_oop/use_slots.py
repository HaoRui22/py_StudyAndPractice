
class Member(object):
    pass

# 尝试给实例绑定属性：
m = Member()
m.name = 'Lily' # 动态绑定
print(m.name)

# 尝试绑定方法：
def set_age(self, age):
    self.age = age

from types import MethodType # 动态地为实例绑定方法

m.set_age = MethodType(set_age, m)
m.set_age(24)
print(m.age)

# 给一个实例绑定的方法对另一个实例不起作用
m1 = Member()
# m1.set_age(25)
# AttributeError: 'Member' object has no attribute 'set_age'

# 给 class 绑定方法后所有实例均可调用
Member.set_age = set_age
m1.set_age(25)

print(m1.age)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能.
# 但是如果想限制实例的属性，则需要定义一个特殊的 __slots__ 变量
class LmtMember(object):
    __slots__ = ('name', 'age') # 用 tuple 元组 定义允许绑定的属性名

m = LmtMember()