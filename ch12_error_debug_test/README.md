- 12.1
  - [do_try.py](./do_try.py)
  - [err.py](./err.py)
  - [err_logging.py](./err_logging.py)
  - [err_raise.py](./err_raise.py)
  - [err_reraise.py](./err_reraise.py)
  - 练习
    - [debug_ex.py](./debug_ex.py)
- 12.2
  - [print2debug.py](./print2debug.py)
  - [do_assert.py](./do_assert.py)
  - [do_logging.py](./do_logging.py)
  - [log2file.py](./log2file.py)
  - [do_pdb.py](./do_pdb.py)
- 12.3
- 12.4

# 12.1 错误处理

在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数`open()`，成功时返回文件描述符（就是一个整数），出错时返回`-1`

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里:

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

错误是`class`，捕获一个错误就是捕获到该class的一个实例，并且它不是凭空产生的，而是有意创建并抛出的。可以根据需要定义一个错误的class，选择好继承关系并用`raise`语句抛出，但在Python已有内置错误类型的情况下，尽量使用内置的错误类型。

Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。

# 12.2 调试

程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。

虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。