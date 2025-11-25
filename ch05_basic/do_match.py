print('Choose Mode (if/match/cmatch/lmatch) :')
mode = (input())
match mode:
    case 'if':
        print('Input Score (A/B/C/D) :')
        score = (input())
        if score == 'A':
            print('A!')
        elif score == 'B':
            print('B~')
        elif score == 'C':
            print('C...')
        elif score == 'D':
            print('D!')
        else:
            print('?What are you fu*king doing man???')
    case 'match':
        print('Input Score (A/B/C/D) :')
        score = (input())
        match score:
            case 'A':
                print('(match)A')
            case 'B':
                print('(match)B')
            case 'C':
                print('(match)C')
            case 'D':
                print('(match)D')
            case _:
                print('?What are you fu*king doing man???')
    case 'cmatch':
        print('Input Age')
        age = int(input())
        match age:
            case x if x < 10:
                print(f'< 10 years old: {x}')
            case 10:
                print('10 years old')
            case 11|12|13|14|15|16|17|18:
                print('11~18 years old')
            case 19:
                print('19 years old')
            case x if 20 <= x <=99:
                print(f'> 19 years old')
            case _:
                print('我不好说。。')
    case 'lmatch':
        print('There Exists a List')
        # args = ['gcc', 'hello.c', 'world.c']
        args = ['clean']
        # args = ['gcc']

        match args:
            # 如果仅出现gcc，报错:
            case ['gcc']:
                print('gcc: missing source file(s).')
            # 出现gcc，且至少指定了一个文件:
            case ['gcc', file1, *files]:
                print('gcc compile: ' + file1 + ', ' + ', '.join(files))
            # 仅出现clean:
            case ['clean']:
                print('clean')
            case _:
                print('invalid command.')