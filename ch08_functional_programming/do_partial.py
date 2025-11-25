# int() 数据类型转换可以通过传入参数 base=N 将数据按 N 进制转换。默认 base=10
s = '12345'
n = int(s)
print(f"s: {s} {type(s)}")
print(f"n: {n} {type(n)}")
n8 = int(s, base=8)
print(f"n8: {n8} {type(n8)}")
n16 = int(s, base=16)
print(f"n16: {n16} {type(n16)}")

# 转换大量二进制字符串，但希望避免每次传入 base=2 参数
def int2(x, base=2):
    return int(x, base)

print(int2('1'))
print(int2('10'))
print(int2('100'))
print(int2('1000'))
print(int2('10000'))
print(int2('100000'))
print(int2('1000000'))
print(int2('10000000'))
print(int2('100000000'))
print(int2('1000000000'))
print(int2('10000000000'))

# functools.partial就是帮助我们创建一个偏函数的
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
print(int2('10000000000'))

# functools.partial的作用就是把一个函数的某些参数固定并返回一个新的函数以便于调用
# 创建偏函数时，实际上可以接收 函数对象、*args、**kw 这3个参数

max10 = functools.partial(max, 10)
m = max10(2, 5, 7)
print(m)
m = max10(2, 5, 7, 11)
print(m)