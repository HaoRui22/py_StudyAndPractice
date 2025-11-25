def my_rev(x):
    if not isinstance(x,(int,float)):
        print('Please input a number...')
    else:
        return -x
while 1:
    print('Input a number(input 4444 to quit):')
    x=int(input())
    if x == 4444:
        print('QUIT NOW')
        break
    else:
        print(my_rev(x))