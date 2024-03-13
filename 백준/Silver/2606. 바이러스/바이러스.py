N = int(input())
K = int(input())
arr = [[] for _ in range(N+1)]

for i in range(K):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (N+1)
def dfs(s, visited):
    if not visited[s]:
        visited[s] = True
        for i in arr[s]:
            dfs(i, visited)

dfs(1,  visited)

print(visited.count(True)-1)
