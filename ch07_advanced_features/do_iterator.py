#迭代器

#可以直接作用于for循环的数据类型：
#数据集合类型：
#list, tuple, dict, set, str
#生成器
#generator, generator function with yield
#以上称为可迭代对象Iterable

#使用 isinstance() 判断是否为Iterable对象
print("Iterable or not ?")
from collections.abc import Iterable
print(f"[]: {isinstance([], Iterable)}")
print(f"'abc': {isinstance('abc', Iterable)}")
print(f"x for x in range(10): {isinstance((x for x in range(10)), Iterable)}")
print(f"100: {isinstance(100, Iterable)}")

print("=== === === === === ===")

#生成器还可以被next()函数不断调用并返回下一个值直到最后抛出StopIteration错误
#可以被next()函数调用并不断返回下一个值的对象被称为迭代器Iterator

#使用 isinstance() 判断是否为Iterator对象
print("Iterator or not ?")
from collections.abc import Iterator
print(f"x for x in range(10): {isinstance((x for x in range(10)), Iterator)}")
print(f"[]: {isinstance([], Iterator)}")
print(f"'abc': {isinstance('abc', Iterator)}")

#使用 iter() 将list, dict, str等Iterable转变成Iterator
print(f"iter([]): {isinstance(iter([]), Iterator)}")
print(f"iter('abc'): {isinstance(iter('abc'), Iterator)}")
