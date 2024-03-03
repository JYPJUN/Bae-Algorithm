T = int(input())

dirs = [(p, q) for p in range(-1, 2) for q in range(-1, 2)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f'#{tc}', result)