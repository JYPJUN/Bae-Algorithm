T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_cnt = 0
    for i in arr:
        if max_cnt < len(i):
            max_cnt = len(i)
    for p in range(len(arr)):
        if len(arr[p]) < max_cnt:
            for j in range(max_cnt-len(arr[p])):
                arr[p].append(' ')
    _arr = list(map(list, zip(*arr)))
    result = ''

    for a in _arr:
        for b in a:
            if b != ' ':
                result += b

    print(f'#{tc}', result)