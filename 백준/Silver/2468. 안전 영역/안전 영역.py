import sys
from collections import deque

def find_safe_area(point, i):
    q = deque([point])
    while q:
        a, b = q.popleft()
        for d in dirs:
            ni, nj = a + d[0], b + d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] > i:
                visited[ni][nj] = True
                q.append((ni, nj))
    return 1

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_cnt = 1

for i in range(1, max(map(max, arr))): # 1부터 arr에 있는 최대 max -1 만큼 다 잠기는거 체크
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for p in range(N):
        for q in range(N):
            if arr[p][q] > i and not visited[p][q]:
                cnt += find_safe_area((p, q), i)

    max_cnt = max(max_cnt, cnt)

print(max_cnt)