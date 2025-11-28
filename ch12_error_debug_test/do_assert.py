# 比 print 大法更好的办法是断言 assert
# 凡是用print()来辅助查看的地方，都可以用断言 assert 来替代：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n

def main():
    foo('0')

# 如果断言失败，assert语句本身就会抛出AssertionError
main()

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert。关闭后，所有的assert≈pass。