from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque([])
minus = 0
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j, 0))
        elif arr[i][j] == -1:
            minus += 1

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
if not q:
    result = -1
elif len(q) + minus == M*N:
    pass
else:
    while q:
        a, b, c = q.popleft()
        for d in dirs:
            ni, nj = a + d[0], b + d[1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                arr[ni][nj] = 1
                q.append((ni,nj,c+1))
        result = c
        
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                result = -1
                break
        if result == -1:
            break

print(result)