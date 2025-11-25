def fact(n):
    if n == 1:
        return n
    elif n == 0:
        return 0
    elif n < 0:
        raise TypeError("请输入非负整数！")
    return n * fact(n - 1)
print(fact(100))

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:])
    + s[0]
print(reverse("gfedcba"))

print("汉诺塔问题递归解决方案：\n" \
    "1.将n-1个盘子从A借助C移动到B\n" \
    "2.将第n个盘子（最大的盘子）从A移动到C\n" \
    "3.将B上的n-1个盘子再借助A移动到C")
def move(n, a, b, c):
    #基线：只有一个盘子，直接移动
    if n == 1:
        print(a,'--->',c)
    else:
        #步骤1
        move(n-1, a, c, b)
        #步骤2
        print(a,'--->',c)
        #步骤3
        move(n-1, b, a, c)

move(3,'A','B','C')
