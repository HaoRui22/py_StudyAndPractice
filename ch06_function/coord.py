import math

def move(x, y, step, angle=0):
    radian = math.radians(angle)
    nx = x + step * math.cos(radian)
    ny = y + step * math.sin(radian)
    return nx, ny

print('Please input x:')
x = float(input())
print('Please input y:')
y = float(input())
print('Please input moved steps:')
step = float(input())
print('Please input moved angle:')
angle = float(input())
print('Result:')
r = move(x, y, step, angle)
print(f"Result: ({r[0]:.6f}, {r[1]:.6f})")