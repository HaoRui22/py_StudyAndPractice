# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 来自 ./_special_iter.py 中的定义
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
# Fib()[5]
# TypeError: 'Fib' object is not subscriptable

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b ,a + b
        return a
    
f = Fib()
f
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])
print(f[10])

# 但是list有个神奇的切片方法：
l = list(range(100))[5:10]
print(l)

# f[5:10]
# TypeError: 'slice' object cannot be interpreted as an integer
# 原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n 是切片
            start = n.start or 0
            stop = n.stop
            step = n.step or 1
            
            if stop is None:
                raise ValueError("There must be a STOP value!")
            a, b = 1, 1
            full = []
            for _ in range(stop):
                full.append(a)
                a, b = b, a + b
            L = full[start:stop:step]
            return L

f = Fib()
print(f[1:10])
print(f[1:10:2])

# 以上 __getitem__ 还没有对负数做处理。所以，要正确实现一个__getitem__()还是有很多工作要做的。

#此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。