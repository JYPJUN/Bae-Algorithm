from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(R)]
q_f = deque([])
q_j = deque([])
for i in range(R):
    for j in range(C):
        if arr[i][j] in 'JF':
            if arr[i][j] == 'F':
                q_f.append((i, j))
            else:
                q_j.append((i, j, 0))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
result = 0
while True:
    M = len(q_f)
    for k in range(M):
        i, j = q_f.popleft()
        for d in dirs:
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in '#F':
                arr[ni][nj] = 'F'
                q_f.append((ni, nj))
    N = len(q_j)
    for kk in range(N):
        a, b, c = q_j.popleft()
        for d in dirs:
            na, nb = a+d[0], b+d[1]
            if 0<=na<R and 0<=nb<C and arr[na][nb] not in '#FK':
                arr[na][nb] = 'K'
                q_j.append((na, nb, c+1))
            elif na>=R or na<0 or nb>=C or nb<0:
                result = c+1
                break
        if result != 0:
            break
    if result != 0 or not q_j:
        break

print(result) if result != 0 else print('IMPOSSIBLE')