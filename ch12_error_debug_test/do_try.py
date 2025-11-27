def some_function():
    print("ok")
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：

def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass

# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
# 所以高级语言通常都内置了一套 try...except...finally... 的错误处理机制，Python 也不例外。

# try 的机制
try:
    print("try...")
    r = 10 / 0
    print(f"result: {r}")
except ZeroDivisionError as err:
    print(f"except: {err}")
finally:
    print("finally...")
print("END")
# 以上内容：
# 当我们认为某些代码可能会出错时，就可以用 try 来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完 except 后，如果有 finally 语句块，则执行 finally 语句块，
# 至此，执行完毕。

# 上面的代码在计算 10÷0 时会产生一个除法运算错误
# 从输出可以看到，当错误发生时，后续语句 print('result:', r) 不会被执行，except 由于捕获到ZeroDivisionError，因此被执行。
# 最后，finally语句被执行。然后，程序继续按照流程往下走。

# 如果将除数改为 2
try:
    print("try...")
    r = 10 / 2
    print(f"result: {r}")
except ZeroDivisionError as err:
    print(f"except: {err}")
finally:
    print("finally...")
print("END")
# 由于没有错误发生，所以 except 语句块不会被执行，但是 finally 如果有，则一定会被执行（可以没有finally语句）。

# 错误有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
try:
    print("try...")
    r = 10 / int('a')
    print(f"result: {r}")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
finally:
    print("finally...")
print("END")
# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。

# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print("try...")
    r = 10 / int('2')
    print(f"result: {r}")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
else:
    print("no error")
finally:
    print("finally...")
print("END")

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
try:
    foo()
except ValueError as e:
    print("ValueError")
except UnicodeError as e:
    print("UnicodeError")
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
# Python所有的错误都是从BaseException类派生的，具体见官方文档

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        print("try...")
        bar('0')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("finally...")

main()

# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。