# map接收一个function和一个iterable并将传入的function依次作用到序列中的每个元素并将结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

# 把list中所有数字转化为字符串
print(list(map(str, L)))


# reduce把一个接收两个函数（必须）的function作用在一个序列[x1, x2, x3, ...]上。reduce会把结果和序列的下一个元素做累积计算
# 类似于 reduce(f, [x1, x2, x3, x4])  f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y

nums = range(1,5)
print(reduce(add, nums))

def fn(x, y):
    return x * 10 + y

num = [1, 3, 5, 7, 9]
print(reduce(fn, num))

# reduce配合map实现str转int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

s = str(input())
print(f"{s}\ntype:{type(s)}")
print(f"{str2int(s)}\ntype:{type(str2int(s))}")

# 练习题代码：mrex1_std.py mrex2_prod.py mrex3_str2float.py
# map用于将一个函数作用于一个序列，以此得到另一个序列；
# reduce用于将一个函数依次作用于上次计算的结果和序列的下一个元素，以此得到最终结果。