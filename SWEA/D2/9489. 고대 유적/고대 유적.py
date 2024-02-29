T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    length = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                a, b, x, y = i, j, 0, 0
                for d in dirs:
                    if 0<=i+d[0]<N and 0<=j+d[1]<M and arr[i+d[0]][j+d[1]] == 1:
                        x, y = d[0], d[1]
                        cnt = 1
                        while True:
                            if 0<=a+x<N and 0<=b+y<M and arr[a+x][b+y] == 1:
                                cnt += 1
                                a += x
                                b += y
                            else:
                                break
                        if length < cnt:
                            length = cnt
    print(f'#{tc}', length)