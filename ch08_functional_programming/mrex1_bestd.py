# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
import sys

def uplo(name):
    if len(name) <= 1:
        print("The name is invalid. Please restart the session and input valid names.")
        sys.exit(1)
    else:
        result = ""
        for i in range(len(name)):
            ch = name[i]
            if i == 0:
                ch = ch.upper()
                result = result + ch
            else:
                ch = ch.lower()
                result = result + ch
        return result

def bestd(names):
    if not names:
        print("The name is invalid. Please restart the session and input valid names.")
        sys.exit(1)
    else:
        Lstd = list(map(uplo, names))
        return(Lstd)

print("Please input names. Press 'Enter' to input next, press 'Enter' again when it's done.")

L1 = []
while 1:
    n = input()
    if n != "":
        L1.append(n)
    else:
        break

print(bestd(L1))
