words = input().split('"')

if len(words) <= 2:
    print('CE')
elif len(words) == 3:
    if len(words[1]) == 0 or len(words[0]) != 0 or len(words[2]) != 0:
        print('CE')
    else:
        print(words[1])