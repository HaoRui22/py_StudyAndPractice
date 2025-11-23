- 类和实例
  - [student.py](./student.py)
- 访问限制
  - [protected_student.py](./protected_student.py)
- 继承和多态
  - [animals.py](./animals.py)
- 获取对象信息
  - [get_object_type.py](./get_object_type.py)
- 实例属性和类属性
  - [attribute.py](./attribute.py)
- 练习
  - [count_stu.py](./count_stu.py)

# 10.1 类和实例

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```

# 10.2 访问限制

# 10.3 继承和多态

继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 10.4. 获取对象信息

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。

如果可以直接写：
```
sum = obj.x + obj.y
```
就不要写：
```
sum = getattr(obj, 'x') + getattr(obj, 'y')
```
一个正确的用法的例子如下：
```
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

# 10.5 实例属性和类属性

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。