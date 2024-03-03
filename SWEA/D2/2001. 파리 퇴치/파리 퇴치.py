T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    dirs = [(i, j) for i in range(M) for j in range(M)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt =0
    for p in range(N):
        for q in range(N):
            cnt = 0
            for d in dirs:
                ni, nj = p + d[0], q + d[1]
                if 0<=ni<N and 0<=nj<N:
                    cnt += arr[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc}', max_cnt)