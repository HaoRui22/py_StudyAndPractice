# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):
    def char2num(c):
        return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    def combine(x, y):
        return x * 10 + y
    inte_part, frac_part = s.split('.')
    inte_num = reduce(combine, map(char2num, inte_part))
    frac_num = reduce(combine, map(char2num, frac_part)) / (10 ** len(frac_part))
    return inte_num + frac_num



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')