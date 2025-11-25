Lo = [1, 23, 66, 2, 3, 7, -5, -9, 0, -99, -1]
Ln = sorted(Lo)
print(f"      正序：{Ln}")

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

Lk = sorted(Lo, key=abs)
print(f"绝对值正序：{Lk}")

# 通过reverse布尔值逆转

Lk = sorted(Lo, key=abs, reverse=True)
print(f"绝对值倒序：{Lk}")

Lk = sorted(Lo, reverse=True)
print(f"      倒序：{Lk}\n")

# 字符串排序按首字母ASCII码

So = ['bob', 'about', 'Zoo', 'Credit']
Sn = sorted(So)
print(f"未优化大小写正序：{Sn}")

Sn = sorted(So, key=str.lower)
print(f"  优化大小写正序：{Sn}")

Sn = sorted(So, key=str.upper, reverse=True)
print(f"  优化大小写倒叙：{Sn}")

'''
练习
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序,再按成绩从高到低排序：
'''

L = [('bob', 75), ('Adam', 92), ('Bart', 66), ('lisa', 88)]

def by_name(t):
    name = str(t[0])
    return name.upper()

L1 = sorted(L, key=by_name)
print(L1)

def by_score(t):
    score = t[1]
    return score

L2 = sorted(L, key=by_score, reverse=True)
print(L2)