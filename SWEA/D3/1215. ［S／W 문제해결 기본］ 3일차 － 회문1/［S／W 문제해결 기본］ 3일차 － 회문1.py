for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    arr.extend([''.join(arr[j][i] for j in range(8)) for i in range(8)])

    cnt = 0

    for n in range(16):
        for k in range(8-N+1):
            if arr[n][k:k+N] == arr[n][k:k+N][::-1]:
                cnt += 1

    print(f'#{tc}', cnt)