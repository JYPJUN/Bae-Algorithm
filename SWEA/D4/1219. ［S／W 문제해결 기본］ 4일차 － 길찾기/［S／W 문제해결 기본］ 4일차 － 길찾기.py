def dfs(i, V):
    visited = [0] * (V+1)
    intersection = []
    visited[i] = 1
    while True:
        if i == 99:
            return 1
        for w in load[i]:
            if w == 99:
                i = w
                break
            elif visited[w] == 0:
                intersection.append(i)
                i = w
                visited[i] = 1
                break
        else:
            if intersection:
                i = intersection.pop()
            else:
                return 0

for tc in range(1, 11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))

    load = [[] for p in range(N+1)]
    for q in range(N):
        n1, n2 = arr[2*q], arr[2*q+1]
        load[n1].append(n2)
    print(f'#{tc}', dfs(0, N))