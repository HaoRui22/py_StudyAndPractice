- 12.1
  - [do_try.py](./do_try.py)
  - [err.py](./err.py)
  - [err_logging.py](./err_logging.py)
  - [err_raise.py](./err_raise.py)
  - [err_reraise.py](./err_reraise.py)
- 12.2
- 12.3
- 12.4

# 12.1 错误处理

在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数`open()`，成功时返回文件描述符（就是一个整数），出错时返回`-1`