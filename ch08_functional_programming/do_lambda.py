l1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(f"l1(use lambda): {l1}")

def f(x):
    return x ** 2

l2 = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(f"l2(use def): {l2}")

# lambda: 匿名函数。语法：lambda x参数 : x*x返回值
#         限制只能有一行表达式
#         返回值就是该表达式的结果
#         匿名函数也是一个函数对象

fl = lambda x: x + 1
print(f)
print(f(1))

# 也可以把 lambda 匿名函数作为返回值返回 ；

def build(x, y):
    return lambda: x * x + y * y

print(build(2, 4))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1,21)))

print(f"L(use def): {L}")

# 使用匿名函数 lambda 改造：

L1 = list(filter(lambda x: x % 2 == 1, range(1,21)))

print(f"L1(use lambda): {L1}")