tc = int(input())

for i in range(1, tc+1):
    N = int(input())

    lst = [[0]*N for _ in range(N)] # N*N 이중 배열
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 / 하 / 좌 / 상
    num = 1 # 채울 숫자
    d = 0 # 이동방향
    x, y = 0, -1 # 시작 위치
    # 달팽이 구간 반복
    while num <= (N**2):
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]
        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
            lst[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            d = (d+1) % 4
    print(f'#{i}')
    for a in lst:
        print(*a)