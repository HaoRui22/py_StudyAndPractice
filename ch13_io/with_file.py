# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('./ch13_io/test.txt', 'r')
# 标示符'r'表示读，这样，我们就成功地打开了一个文件。

# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
print(f.read())

# 调用close()方法关闭文件。
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
print("use try...finally")
try:
    f = open('./ch13_io/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 上种写法相对繁琐，而 Python 引入了 with 语句来帮助自动调用 close()
print("use with")
with open('./ch13_io/test.txt', 'r') as f:
    print(f.read())
# 此写法等价于上面的 try...finally

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
    print("readlines()")
    f.seek(0) # 重置指针到开头
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
    print("over")

# 前面默认都是读取文本文件，并且是UTF-8编码。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('./ch13_io/test.jpg', 'rb')
print(f.read())
f.close()

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如GBK
f = open('./ch13_io/gbk.txt', 'r', encoding='gbk')
print(f.read())
f.close