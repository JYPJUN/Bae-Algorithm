from collections import deque

def solution(n, edge):

    arr = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i in range(len(edge)):
        arr[edge[i][0]].append(edge[i][1])
        arr[edge[i][1]].append(edge[i][0])

    q = deque([(1, 1)])
    while q:
        a, b = q.popleft()
        if not visited[a]:
            visited[a] = b
            for i in arr[a]:
                q.append((i, b+1))

    answer = visited.count(max(visited))
    return answer