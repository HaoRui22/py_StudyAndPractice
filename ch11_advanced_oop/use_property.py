import ch10_oop.student as student
import ch10_oop.protected_student as protected_student
from datetime import date

class PpStudent(object):
    def __init__(self, score = 0):
        self.__score = score

    @property # 定义 getter 方法，将其包装成属性
    def score(self):
        return self.__score
    
    @score.setter # 此装饰器是 @property 创建的，负责把 setter 方法变成属性赋值，由此得到一个可控的属性操作
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('bad input')
        if value < 0 or value > 100:
            raise ValueError('bad score')
        self.__score = value
    
    @property # 同上定义 getter 。可读
    def birthYear(self):
        return self.__birthYear

    @birthYear.setter # 可写
    def birthYear(self, value):
        self.__birthYear = value

    @property # 只有 getter，没有 setter，只读
    def age(self):
        return date.today().year - self.__birthYear
        


if __name__ == '__main__':

# 绑定属性时直接把属性暴露出去，编写简单但无法进行参数检查：
    s = student.Student()
    s.score = 9999
    print(f"分数{s.score}显然不合逻辑")

# 想限制 score 范围，可以通过方法 set_score() get_score() 来设置和获取成绩，在set_score()方法里就可以检查参数：
# 如同 ../ch10_oop/protected_student.py中定义类的做法
    ps = protected_student.PtStudent()
    ps.set_score(100)
    print(ps.get_score())
    # ps.set_score(-1)
    # ValueError: bad score

# BUT... 在../ch10_oop/protected_student.py中定义类的做法略显复杂
# 想追求完美，既能检查参数又可以用类似属性这样的简单方式访问类的变量，则需要用到装饰器
# Python内置的@property装饰器就是负责把一个方法变成属性调用的。请查看类⬆️：PpStudent
    print("use property⬇️")
    pps = PpStudent()
    pps.score = 60
    print(pps.score)
    # pps.score = 110
    # ValueError: bad score
    # 设置读写属性 birthYear
    pps.birthYear = 2001
    # 读取
    print(pps.birthYear)
    # 读取只读属性
    print(pps.age)