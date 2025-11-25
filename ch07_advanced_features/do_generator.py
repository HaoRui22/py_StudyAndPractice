L = [x * x for x in range(10)]
#print(f"[列表生成式]L:{L}")
g = (x * x for x in range(10))
#print(g)

#for n in g:
    #print(n)

#Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
n = 6
#print('Fibonacci n:')
#fib(n)
#Fibonacci
def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for n in fibg(6):
    print(n)

g = fibg(6)

while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
#print(next(o))
