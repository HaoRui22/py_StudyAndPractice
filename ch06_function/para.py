#位置参数
print('位置参数')
def square(x):
    return x * x
#+默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n-1
    return s
s = power(9)
print(s)

#可变参数
print('可变参数')
def squsum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n * n
    return sum
r = squsum (1,2,3)
print(r)
t = [1,2,3,4]
print(t)
r = squsum(*t)
print(r)

#关键字参数
print('关键字参数')
def person(name, age, **kw):
    record = f'Name: {name},\nAge: {age}, \nOther: {kw}'
    return record

p1 = person('Zane',25,Gender='man',Job='engineer')
print(p1)
p2 = person('闫利锐',25,性别='女',年龄='25',职业='研究生',性格='温柔')
print(p2)
extra = {'gender':'woman','job':'student'}
p3 = person('Avery',25,Gender=extra['gender'],Job=extra['job'])
print(p3)
p4 = person('Avery',25,**extra)
print(p4)
#命名关键字参数
print('命名关键字参数')
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('Name:', name,'Age:', age, 'Other:', kw)
person('Zach', 24, city='Langfang',addr='Guangyang',postcode = '065000')


#参数组合
print('参数组合 顺序：必选-默认-可变-命名关键字-关键字')
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =',kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print('必选')
f1(1, 2)
print('必选+默认')
f1(1, 2, c=3)
print('必选+默认+可变')
f1(1, 2, 3, 'a', 'b')
print('必选+默认+可变+关键')
f1(1, 2, 3, 'a', 'b', x=99)
print('必选+命名关键字+关键字')
f2(1, 2, d=99, ext=None, test=1)
print('通过tuple元组和dict字典也可以调用上述函数：')
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)