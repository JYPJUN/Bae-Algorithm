N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False] * N for i in range(N)]
N_color = ['R', 'G', 'B']
A_color = ['RG', 'B']
AA, BB = 0, 0
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
for i in range(N):
    for j in range(N):
        for p in N_color:
            stack = []
            if not visited[i][j] and arr[i][j] == p:
                stack.append((i, j))
                while stack:
                    a, b = stack.pop()
                    visited[a][b] = True
                    for d in dirs:
                        ni, nj = a+d[0], b+d[1]
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == p and not visited[ni][nj]:
                            stack.append((ni, nj))
                AA += 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for p in A_color:
            stack = []
            if not visited[i][j] and arr[i][j] in p:
                stack.append((i, j))
                while stack:
                    a, b = stack.pop()
                    visited[a][b] = True
                    for d in dirs:
                        ni, nj = a+d[0], b+d[1]
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] in p and not visited[ni][nj]:
                            stack.append((ni, nj))
                BB += 1
print(AA, BB)