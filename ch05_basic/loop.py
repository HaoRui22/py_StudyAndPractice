print('Welcome to LOOP demo\n' \
'Mode:\n' \
'1:for name in names\n' \
'2:for x in a list\n' \
'3:for x in range\n' \
'4:while\n' \
'5:exam\n' \
'6:break\n' \
'7:continue\n' \
'8:break\n' \
'Choose mode:')
mode = (input())
match mode:
    case '1':
        print('ready---------------')
        names = ['Michael','Bob','Tracy']
        for name in names:
            print(name)
    case '2':
        print('sum=0---------------')
        sum = 0
        for x in [1,2,3,4,5,6,7,8,9,10]:
            sum = sum +x
            print(sum)
        print('sum is',sum)
    case '3':
        print('sum=0-range(101)----')
        sum = 0
        for x in range(101):
            sum = sum + x
        print(sum)
    case '4':
        print('sum=0-----while-----')
        sum = 0
        n = 99
        while n > 0:
            sum = sum+n
            n = n - 2
            #print(sum)
        print(sum)
    case '5':
        print('exam----------------')
        L = ['Bart','Lisa','Adam']
        for name in L:
            print('Hello, %s !'%(name))
        print('Over.')
    case '6':
        print('break---------------')
        n = 0
        while n < 100:
            
            n = n + 1
            if n > 10:
                break
            print(n)
        print('END')
    case '7':
        print('continue------------')
        print('without continue')
        n = 0
        while n < 10:
            n = n + 1
            print(n)
        print('with continue')
        n = 0
        while n < 10:
            n = n + 1
            if n % 2 == 0:
                continue
            print(n)
    case '8':
        print('break---------------')
        n = 0
        while n < 10:
            n = n + 1
            print(n)
            if n == 5:
                break
