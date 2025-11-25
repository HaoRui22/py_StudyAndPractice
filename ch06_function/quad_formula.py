import math

def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    if x1 == x2:
        return x1
    else:
        return x1, x2
    
print('→ ax²+bx+c=0')
print('Input a and b and c(use ENTER):')
a = float(input())
b = float(input())
c = float(input())
print('Result:')
r = quadratic(a,b,c)
print(r)