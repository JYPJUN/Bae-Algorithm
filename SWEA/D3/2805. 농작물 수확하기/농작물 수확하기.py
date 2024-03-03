T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    cnt = 0
    a = 0
    for i in range(N):
        if N == 1:
            cnt = arr[0][0]
        elif i < N//2:
            cnt += sum(arr[i][(N//2)-a:(N//2)+a+1])
            a += 1
        elif i == N//2:
            cnt += sum(arr[i][(N//2)-a:(N//2)+a+1])
        else:
            a -= 1
            cnt += sum(arr[i][(N//2)-a:(N//2)+a+1])

    print(f'#{tc}', cnt)