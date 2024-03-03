T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = [[arr[i][j] for i in range(N-1, -1, -1)] for j in range(N)]
    arr_180 = [[arr_90[i][j] for i in range(N-1, -1, -1)] for j in range(N)]
    arr_270 = [[arr_180[i][j] for i in range(N - 1, -1, -1)] for j in range(N)]

    print(f'#{tc}')
    for a in range(N):
        print(''.join(map(str, arr_90[a])) + ' ' + ''.join(map(str, arr_180[a])) + ' ' + ''.join(map(str, arr_270[a])))