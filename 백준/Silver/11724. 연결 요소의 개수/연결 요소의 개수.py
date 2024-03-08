from collections import deque
import sys
def bfs(start, arr, visited):
    q = deque([start])
    visited[start] = True
    while q:
        k = q.popleft()
        for i in arr[k]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
for j in range(1, N+1):
    if not visited[j]:
        bfs(j, arr, visited)
        cnt += 1
        
print(cnt)