import os

l1 = list(range(1, 16))
print(l1)

l1 = []
for x in range(1,11):
    l1.append(x * x)
print(l1)

l1 =[]
print(l1)
l1 = [x * x for x in range(1,12)]
print(l1)
l1 = [x * x for x in range(1,11) if x % 2 == 0]
print(l1)
l1 = [x + y for x in 'ABC' for y in 'abc']
print(l1)

# os.listdir可以列出文件和目录
ls = [d for d in os.listdir('.')]
print(ls)

#for循环可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

l1 = [k + '=' + v for k, v in d.items()]
print(l1)

L = ['Hello', 'World', 'Kali', 'Ubuntu', 'Arch']
print(L)
l1 = [s.lower() for s in L]
print(l1)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')