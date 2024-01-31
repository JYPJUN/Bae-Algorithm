tc = int(input())
 
for i in range(1, tc+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dir_r = []
    dir_d = []
    for n in range(K):
        dir_r.append((0, n))
    for m in range(K):
        dir_d.append((m, 0))
 
    cnt = 0
    # 가로행
    for j in range(N):
        for k in range(N-K+1):
            result = 0
            for d in dir_r:
                nk = k + d[1]
                result += lst[j][nk]
            if result == K:
                if nk == N-1 and lst[j][k-1] != 1:
                    cnt += 1
                elif k == 0 and lst[j][nk+1] != 1:
                    cnt += 1
                elif 1 <= k and nk < N-1:
                    if lst[j][k-1] != 1 and lst[j][nk+1] != 1:
                        cnt += 1
 
    # 세로행
    for j in range(N-K+1):
        for k in range(N):
            result = 0
            for d in dir_d:
                nj = j + d[0]
                result += lst[nj][k]
            if result == K:
                if nj == N - 1 and lst[j-1][k] != 1:
                    cnt += 1
                elif j == 0 and lst[nj+1][k] != 1:
                    cnt += 1
                elif 1 <= j and nj < N - 1:
                    if lst[j-1][k] != 1 and lst[nj+1][k] != 1:
                        cnt += 1
 
    print(f'#{i}', cnt)