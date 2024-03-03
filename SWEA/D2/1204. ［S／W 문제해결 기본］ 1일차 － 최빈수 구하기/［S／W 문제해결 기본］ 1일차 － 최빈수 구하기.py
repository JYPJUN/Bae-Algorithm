T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    point = [0]*101
    for i in arr:
        point[i] += 1

    print(f'#{tc}', 100 - point[::-1].index(max(point)))