# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
JAN = 1
FEB = 2
MAR = 3 
# 好处是简单，缺点是类型是 int，并且仍然是变量

# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
# Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了'Month'类型的枚举。
# 可以直接使用 Month.Jan 来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    # value 属性则是自动赋给成员的 int 常量，默认从1开始计数
    print(name, '=>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从 Enum 派生出自定义类：
from enum import unique

@unique # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7

# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Wed'])

print(Weekday.Thu.value)

print(Weekday(5))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。