T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir_X = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    dir_T = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for p in range(1, M):
                for d in dir_X:
                    ni = i + d[0] * p
                    nj = j + d[1] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
            cnt += arr[i][j]
            for p in range(1, M):
                for d in dir_T:
                    ni = i + d[0] * p
                    nj = j + d[1] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc}', max_cnt)

