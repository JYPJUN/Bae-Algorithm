tc = int(input())
 
for i in range(1, tc+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dir = []
    for j in range(M):
        for n in range(M):
            dir.append((j, n))
 
    bug_lst = []
    for k in range(N-M+1):
        for m in range(N-M+1):
            result = 0
            for d in dir:
                ni = k + d[0]
                nj = m + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    result += lst[ni][nj]
            bug_lst.append(result)
    print(f'#{i}', max(bug_lst))