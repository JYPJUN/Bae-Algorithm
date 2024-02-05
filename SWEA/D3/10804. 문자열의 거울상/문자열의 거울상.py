T = int(input())

for tc in range(1, T+1):
    str1 = input()
    result = ''

    pre_str = [i for i in str1]

    for j in range(len(pre_str)-1, -1, -1):
        if pre_str[j] == 'b':
            result += 'd'
        elif pre_str[j] == 'd':
            result += 'b'
        elif pre_str[j] == 'p':
            result += 'q'
        else:
            result += 'p'

    print(f'#{tc}', result)