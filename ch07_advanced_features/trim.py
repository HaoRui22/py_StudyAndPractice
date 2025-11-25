#使用切片去除字符串首尾空格
def trim(s):
    #头下标
    start = 0
    #尾下标
    end = len(s) - 1
    #数除开头空格
    while start < len(s) and s[start] == ' ':
        start += 1
    #数除结尾空格
    while end >= 0 and s[end] == ' ':
        end -= 1
    #判断空字符串
    if start > end:
        return ''
    #返回结果
    else:
        return s[start:end+1]

print(trim('        Ok        '))

# 测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')