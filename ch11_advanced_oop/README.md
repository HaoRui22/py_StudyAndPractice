- 11.1 使用`__slots__`
  - [use_slots.py](./use_slots.py)
- 11.2 使用`__slots__`
  - [use_property.py](./use_property.py)
  - 练习
    - [object_screen.py](./object_screen.py)
- 11.3 多重继承
  - [multi_animals.py](./multi_animals.py)
- 11.4 定制类
  - [_special_str.py](./_special_str.py)
  - [_special_iter.py](./_special_iter.py)
  - [_special_getitem.py](./_special_getitem.py)
  - [_special_getattr.py](./_special_getattr.py)
  - [_special_call.py](./_special_call.py)
- 11.5 使用枚举类
  - [use_enum.py](./use_enum.py)
  - 练习
    - [stu_enum.py](./stu_enum.py)
- 11.6 使用元类
  - [creat_class_on_the_fly.py](./creat_class_on_the_fly.py)
  - [use_metaclass.py](./use_metaclass.py)
  - [orm.py](./orm.py)

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

```py
@属性名.setter
```

没有 setter 的属性是只读属性。

3. 为什么要使用 @property

它让你可以用“访问属性”的方式来调用逻辑，而不是方法调用：
```py
s.age = 20     # setter
print(s.age)   # getter
```

但同时可以在 setter 中加入类型检查、范围检查等逻辑：

```py
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

看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考[Python的官方文档](http://docs.python.org/3/reference/datamodel.html#special-method-names)。

- `__str__()` & `__repr__()`
  - `__str__()`：定义对象被 `print(obj)` 或 `str(obj)` 时的字符串表现形式 — 可以让输出更友好、可读。


  - `__repr__()`：定义对象在解释器里（或通过 repr(obj) / 当你直接敲变量名时）被“原样”显示时的表示。通常用于调试，便于开发者查看对象的“官方”表示。


  - 很常见的做法是让 `__repr__ = __str__`，也就是说两种情境下输出一样。


- `__iter__()` & `__next__()`

  - 如果一个类定义了 `__iter__()`（返回一个迭代器对象）和 `__next__()`，那么这个类的实例就可以被 for … in 用来循环，就像列表、元组那样。


  - 这样你就可以让自定义对象表现得像一个“可遍历容器 / 序列”。


- `__getitem__()`

  - 定义后，可以通过 `obj[key]` （例如索引 `obj[0]`，或者使用切片 `obj[2:5]`）来访问对象内部的数据 / 子元素，就像列表或字典那样。


  - 如果你同时提供 `__setitem__()` / `__delitem__()`，还可以实现赋值和删除操作，从而让对象变得更像可变容器（list 或 dict）那样。


- `__getattr__()`

  - 当访问一个对象的属性，但该属性不存在时，如果定义了 `__getattr__()`，Python 会调用它尝试返回一个值，而不是直接报错。这样可以动态地“响应”某些属性。


  - 适合用于那些属性名不固定 / 运行时决定 / 想对某些属性做“延迟计算 / 动态提供值”的场景。


- `__call__()`

  - 定义之后，类的实例可以像函数那样被调用：`instance()`。这意味着你既可以把对象当成“数据 + 方法”的类实例，也可以当成“可调用对象 / 函数”。


  - 提供了把对象和函数视为“同一种东西”的灵活性，有时候方便把逻辑封装成“对象+状态+行为”。

# 11.5 使用枚举类

`Enum`可以把一组相关常量定义在一个`class`中，且`class`不可变，而且成员可以直接比较。

枚举类`Enum`可以动态创建：

```py
Month = Enum('Month',('Jan', 'Feb', 'Mar', ..., 'Dec'))
```

等价于

```py
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    ...
    Dec = 12
```

动态创建时枚举成员的名称列表不需要写等号或数字。`Enum`会自动从`1`开始编号

`Enum`成员的固定核心属性：

| 属性          | 含义                   |
| ----------- | -------------------- |
| `name`      | 枚举成员的名称字符串，如 `"Jan"` |
| `value`     | 枚举成员的底层值，如 `1`       |
| `__class__` | 它所属的枚举类，例如 `Month`   |

枚举值本质上就是 (name, value) 的绑定实例。

# 11.6 使用元类