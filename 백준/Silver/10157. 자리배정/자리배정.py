C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌

cnt = 1
result = [1, 1]
x, y = R-1, 0
arr[x][y] = cnt
n = 0

if C * R < K:
    result = [0]
else:
    while cnt != K:
        ni = x + dirs[n][0]
        nj = y + dirs[n][1]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
            cnt += 1
            arr[ni][nj] = cnt
            x, y = ni, nj
            if cnt == K:
                result = [nj+1, R-ni]
        else:
            n += 1
            if n > 3:
                n %= 4

print(*result)
