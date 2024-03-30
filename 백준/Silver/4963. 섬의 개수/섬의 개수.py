import sys
sys.setrecursionlimit(5000)

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(point):
    x, y = point

    for d in dirs:
        ni, nj = x+d[0], y+d[1]
        if 0 <= ni < b and 0 <= nj < a and not visited[ni][nj] and arr[ni][nj] ==1:
            visited[ni][nj] = True
            dfs((ni, nj))

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]
    visited = [[False]*a for _ in range(b)]

    cnt = 0
    for i in range(b):
        for j in range(a):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs((i, j))
                cnt += 1

    print(cnt)