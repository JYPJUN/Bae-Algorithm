T = int(input())

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_numbers = 0
    for i in range(N):
        for j in range(M):
            numbers = arr[i][j]
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    numbers += arr[ni][nj]
            if max_numbers < numbers:
                max_numbers = numbers
                
    print(f'#{tc}', max_numbers)