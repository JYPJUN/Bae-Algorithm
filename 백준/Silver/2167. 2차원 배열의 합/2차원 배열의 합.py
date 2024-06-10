import sys
I = sys.stdin.readline

N, M = map(int, I().split())

arr = [list(map(int, I().split())) for _ in range(N)]

T = int(I())

for tc in range(T):
    i, j, x, y = map(int, I().split())
    total_sum = 0

    for a in range(i-1, x):
        total_sum += sum(arr[a][j-1:y])
    print(total_sum)