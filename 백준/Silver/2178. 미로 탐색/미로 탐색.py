from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

que = deque([(0, 0, 1)])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while que:
    a, b, c = que.popleft()
    if a == N - 1 and b == M - 1:
        print(c)
        break
    for d in dirs:
        ni, nj = a + d[0], b + d[1]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '1':
            arr[ni] = arr[ni][:nj] + '0' + arr[ni][nj + 1:]
            que.append((ni, nj, c + 1))