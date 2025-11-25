# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def prod(L):
    if not L:
        return 0
    def mult(x1, x2):
        return x1 * x2
    return reduce(mult, L)

L = []
print("Input the numbers that you want to multiply. Press 'Enter' again when it's done.")

while True:
    user_input = input()
    if user_input == "":
        break
    try:
        n = int(user_input)
        L.append(n)
    except ValueError:
        print("Please input a VALID number.")

print(prod(L))