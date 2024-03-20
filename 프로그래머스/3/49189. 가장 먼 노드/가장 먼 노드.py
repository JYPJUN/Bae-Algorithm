from collections import deque

def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for a, b in edge:
        arr[a].append(b)
        arr[b].append(a)

    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        if not visited[x]:
            visited[x] = y
            for i in arr[x]:
                q.append((i, y+1))

    answer = visited.count(max(visited))
    return answer