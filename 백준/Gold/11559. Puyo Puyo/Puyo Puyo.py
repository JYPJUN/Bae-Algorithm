from collections import deque

arr = [list(input()) for _ in range(12)]
r_arr = list(map(list, zip(*arr)))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
colors = ['R', 'G', 'B', 'P', 'Y']
combo = 0
cnt = 0
while cnt != 2:
    visited = [[False] * 12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            for color in colors:
                pre_q = []
                pre_p = deque([])
                if r_arr[i][j] == '.':
                    break
                else:
                    if r_arr[i][j] == color and not visited[i][j]:
                        pre_q.append((i, j))
                        pre_p.append((i, j))
                        visited[i][j] = True
                        while pre_p:
                            a, b = pre_p.popleft()
                            for d in dirs:
                                ni, nj = a+d[0], b+d[1]
                                if 0<=ni<6 and 0<=nj<12 and r_arr[ni][nj] == color and not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    pre_q.append((ni, nj))
                                    pre_p.append((ni, nj))
                        if len(pre_q) >= 4:
                            cnt = 1
                            for x, y in pre_q:
                                r_arr[x][y] = '.'
    if cnt == 1:
        for i in range(6):
            lst = []
            for j in range(12):
                if r_arr[i][j] != '.':
                    lst.append(r_arr[i][j])
                    r_arr[i][j] = '.'
            for z in range(len(lst)):
                r_arr[i][-1-z] = lst[-1-z]

        combo += 1
        cnt = 0
    else:
        cnt = 2

print(combo)