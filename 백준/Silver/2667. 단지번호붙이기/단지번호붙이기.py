import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque([])
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

lst = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == '1':
            q.append((i, j))
            visited[i][j] = True
        if q:
            cnt = 1
            while q:
                a, b = q.popleft()
                for d in dirs:
                    ni, nj = a+d[0], b+d[1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
                        cnt += 1
            lst.append(cnt)
lst.sort()
print(len(lst))
for n in lst:
    print(n)