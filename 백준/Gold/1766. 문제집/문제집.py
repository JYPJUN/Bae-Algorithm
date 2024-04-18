import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
heap = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
q = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    heap[a].append(b)
    visited[b] += 1

for i in range(1, N+1):
    if visited[i] == 0:
        heapq.heappush(q, i)

arr = []
while q:
    k = heapq.heappop(q)
    arr.append(k)
    for i in heap[k]:
        visited[i] -= 1
        if visited[i] == 0:
            heapq.heappush(q, i)

print(*arr)
