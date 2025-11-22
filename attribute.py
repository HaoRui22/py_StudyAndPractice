# 实例属性和类属性
import student
# python 语言是动态的，因此根据类创建的实例可以任意绑定属性

#给实例绑定属性，通过实例变量或 self 变量：
s = student.Student('Bob')

s.score = 90

print(s.name)
print(s.gender)
print(s.score)

# 如果 Student 本身需要绑定一个属性，可以直接在 class 中定义
# 这种属性是类属性，归 Student 类所有
# 比如在 student.py 中的 Student 类定义时添加 name = 

# 定义一个类属性后，属性归类所有，但所有实例都可以访问到。创建一个新 Student 类来测试：
class NewStudent(object):
    name = 'newstu'
# 创建实例s
s = NewStudent()
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

# 给实例绑定属性
s.name = 'Yeliry'
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

# 但类属性仍然存在
print(NewStudent.name)

# 删除实例的 name 属性
del s.name
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

#在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#练习题代码文件：count_stu.py