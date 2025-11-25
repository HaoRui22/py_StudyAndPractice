# 通常情况下的求和函数

def cacl_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 不需要立刻求和而是在后面代码中根据需要计算：可以不返回求和的结果，而是返回求和函数

def lazy_sum(*args):
    def cacl_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return cacl_sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
print(f == f)
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f)
print()

# 闭包（注意：这是演示“延迟绑定 / late binding”）
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i    # 这里的 i 不是快照，是对外层变量 i 的引用（late binding）
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 返回的三个函数都引用同一个循环变量 i（不是每次循环的值快照）。
# 循环结束后 i 的最终值为 3，所以调用时返回的是 3*3 = 9。
print(f"f1: {f1()} ; f2: {f2()} ; f3: {f3()}")

# 如何把“当时的 i 值”作为快照保存？方法之一：把值作为默认参数，
# 默认参数在函数定义时就求值，因此可以把当前 i 的值“锁定”下来。
def count1():
    fs = []
    for i in range(1, 4):
        def f(i=i):    # 把当前循环的 i 的值作为默认值锁定（快照）
            return i*i
        fs.append(f)
    return fs

f4, f5, f6 = count1()
print("使用默认值锁定参数：")
print(f"f4: {f4()} ; f5: {f5()} ; f6: {f6()}")

# 另一种方法：再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
print("二层函数/工厂函数：")
f7, f8, f9 = count2()
print(f"f7: {f7()} ; f8: {f8()} ; f9: {f9()}")

# nonlocal
# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inc():
    x = 0
    def fn():
        # 仅读取x的值
        return x + 1
    return fn

f = inc()
print("\n仅读取外层变量值：")
print(f())
print(f())

# BUT若对外层变量赋值， Py 解释器就会把外层变量当做内部函数的局部变量，然而作为局部变量它并没有被初始化......
def inc1():
    x = 0
    def fn():
        # 想引用 inc() 函数内部的 x，就要在 f() 函数的内部加一个 nonlocal x 声明使解释器把 x 看作外部函数的局部变量
        # 注释掉 nonlocal x 函数则会报错
        nonlocal x
        x = x + 1
        return x
    return fn

f1 = inc1()
print("使用 nonlocal x 声明：")
print(f1())
print(f1())
print(f1())

# 练习题代码：closure_createCounter.py