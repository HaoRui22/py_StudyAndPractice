- 11.1 使用`__slots__`
  - [use_slots.py](./use_slots.py)
- 11.2 使用`__slots__`
  - [use_property.py](./use_property.py)
  - 练习
    - [object_screen.py](./object_screen.py)
- 11.3 多重继承
  - [multi_animals.py](./multi_animals.py)


# 11.1 使用`__slots__`

当我们定义了一个`class`并创建了一个`class`实例后，我们可以给该实例绑定任何属性和方法，这是动态语言的特性。

如果我们想要限制实例的属性，在定义 class 时需要定义一个特殊的变量 `__slots__`，`__slots__` 可以指向一个元组，元组内是允许绑定的属性名称。

`__slots__`近对当前类的实例生效，对其继承子类不生效，而在定义继承子类时定义`__slots__`，则继承子类的实例允许绑定的属性则为该子类的`__slots__` + 其父类的`__slots__`。

# 11.2 使用`@property`

`@property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

1. `@property`的作用

@property 是 Python 内置的描述符，用于将方法转换为受控属性。
它允许：

- 读取时调用 getter 方法

- 写入时调用 setter 方法（如果定义了 setter）

- 删除时调用 deleter 方法（如果定义了 deleter）

这样既能保持接口简洁，又能保证数据的合法性。

2. getter 与 setter 的本质

使用 @property 装饰的方法会变成一个 property 对象：
```
属性访问 → property.__get__ → 调用 getter 方法
属性写入 → property.__set__ → 调用 setter 方法（若定义）
```

setter 并不会自动生成，必须显式使用：
```
@属性名.setter
```

没有 setter 的属性是只读属性。

3. 为什么要使用 @property

它让你可以用“访问属性”的方式来调用逻辑，而不是方法调用：
```
s.age = 20     # setter
print(s.age)   # getter
```

但同时可以在 setter 中加入类型检查、范围检查等逻辑：
```
@score.setter
def score(self, value):
    if not isinstance(value, int):
        raise TypeError("score must be int")
    if not (0 <= value <= 100):
        raise ValueError("score must be between 0 and 100")
    self.__score = value
```

从而避免外部传入非法值，降低错误概率。

4. 属性可写性

有 getter + 有 setter → 可读可写

只有 getter → 只读

有 getter + setter + deleter → 可管理删除逻辑

# 11.3 多重继承

由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如Java）不能使用MixIn的设计。

# 11.4 定制类

# 11.5 使用枚举类

# 11.6 使用元类