# filter()接收一个函数和一个序列，把传入的函数依次作用于序列的每个元素，然后根据返回值是True还是False决定保留还是丢弃元素

def is_odd(n):
    return n % 2 == 1

L = range(0, 36)

Lodd = list(filter(is_odd, L))

print(Lodd)


def not_empty(s):
    return s and s.strip()
s = ['A', '', 'B', None, 'C', '  ']
print(list(filter(not_empty, s)))

# 用filter求素数

def _odd_iter():
    # 这是一个无限奇数序列生成器
    n = 1
    while True:
        n = n + 2
        yield n
# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 定义生成器不断返回下一个素数
def primes():
    yield 2
    ite = _odd_iter() # 初始序列
    while True:
        n = next(ite) # 返回序列的第一个值
        yield n
        ite = filter(_not_divisible(n), ite) # 构造新序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break

# 练习题代码：palindrome.py