for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while arr[-1] > 0:
        arr[0] -= i
        k = arr.pop(0)
        arr.append(k)
        i += 1
        if i > 5: i %= 5

    arr[-1] = 0

    print(f'#{tc}', *arr)