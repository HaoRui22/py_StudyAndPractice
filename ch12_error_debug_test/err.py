# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

# 执行，结果如下：
# $ python3 err.py
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# 出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：
# 错误信息第1行：
# Traceback (most recent call last):
# 告诉我们这是错误的跟踪信息。
# 第2~3行：
#   File "err.py", line 11, in <module>
#     main()
# 调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：
#   File "err.py", line 9, in main
#     bar('0')
# 调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
#   File "err.py", line 6, in bar
#     return foo(s) * 2
# 原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# 原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
# ZeroDivisionError: integer division or modulo by zero
# 根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。