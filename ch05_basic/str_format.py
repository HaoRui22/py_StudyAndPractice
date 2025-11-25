"""
占位符       替换内容
%d          整数
%f          浮点数
%s          字符串
%x          十六进制整数
"""
name = 'L'
print('Hello %s' %(name))

print('%2d-%05d'% (3, 1))

print('%.2f'% 3.1415926)

#format方法
print('{0}-{1:02d}'.format(3, 1)) 

