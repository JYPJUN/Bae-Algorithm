import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

for od in order:
    if od == 1:
        array = array[::-1]
    elif od == 2:
        array = [row[::-1] for row in array]
    elif od == 3:
        array = [[array[N-1-j][i] for j in range(N)] for i in range(M)]
        N, M = M, N
    elif od == 4:
        array = [[array[i][M-1-j] for i in range(N)] for j in range(M)]
        N, M = M, N
    elif od == 5:
        half_N, half_M = N // 2, M // 2
        new_array = [[0] * M for _ in range(N)]

        for i in range(half_N):
            for j in range(half_M):
                new_array[i][j + half_M] = array[i][j]
        
        for i in range(half_N):
            for j in range(half_M, M):
                new_array[i + half_N][j] = array[i][j]
        
        for i in range(half_N, N):
            for j in range(half_M, M):
                new_array[i][j - half_M] = array[i][j]
        
        for i in range(half_N, N):
            for j in range(half_M):
                new_array[i - half_N][j] = array[i][j]

        array = new_array

    elif od == 6:
        half_N, half_M = N // 2, M // 2
        new_array = [[0] * M for _ in range(N)]

        for i in range(half_N):
            for j in range(half_M):
                new_array[i + half_N][j] = array[i][j]
        
        for i in range(half_N, N):
            for j in range(half_M):
                new_array[i][j + half_M] = array[i][j]
        
        for i in range(half_N, N):
            for j in range(half_M, M):
                new_array[i - half_N][j] = array[i][j]
        
        for i in range(half_N):
            for j in range(half_M, M):
                new_array[i][j - half_M] = array[i][j]

        array = new_array

for row in array:
    print(*row)
