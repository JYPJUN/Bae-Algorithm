import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for i in range(N)]
start_point = (0, 0, 0)
check = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start_point = (i, j, 0)
            check = 1
            break
    if check == 1:
        break

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(value):
    que = deque([(value)])
    visited[value[0]][value[1]] = True
    while que:
        a, b, c = que.popleft()
        arr[a][b] = c
        for d in dirs:
            ni = a + d[0]
            nj = b + d[1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 0:
                visited[ni][nj] = True
                que.append((ni, nj, c+1))

bfs(start_point)

for p in range(N):
    for q in range(M):
        if arr[p][q] == 1 and visited[p][q] == False:
            arr[p][q] = -1

for n in arr:
    print(*n)