import sys

N, M = map(int, sys.stdin.readline().split())

P = int(sys.stdin.readline())

arr = []
for i in range(P+1):
    arr.append(list(map(int, sys.stdin.readline().split())))
    # 1-북 / 2-남 / 3-서 / 4-동
way = [1, 4, 2, 3]
result = 0
for j in range(P):
    if abs(way.index(arr[-1][0]) - way.index(arr[j][0])) == 2:
        if arr[-1][0] == 1 or arr[-1][0] == 2:
            left = arr[-1][1] + arr[j][1]
            right = 2*N - left
            result += min(left, right) + M
        else:
            _up = arr[-1][1] + arr[j][1]
            _down = 2*M - _up
            result += min(_up, _down) + N
    elif way.index(arr[-1][0]) == way.index(arr[j][0]):
        result += abs(arr[-1][1]-arr[j][1])
    else:
        if arr[-1][0] == 1:
            if arr[j][0] == 3:
                result += arr[-1][1] + arr[j][1]
            else:
                result += N - arr[-1][1] + arr[j][1]
        elif arr[-1][0] == 2:
            if arr[j][0] == 3:
                result += arr[-1][1] + M - arr[j][1]
            else:
                result += N - arr[-1][1] + M - arr[j][1]
        elif arr[-1][0] == 3:
            if arr[j][0] == 1:
                result += arr[-1][1] + arr[j][1]
            else:
                result += M - arr[-1][1] + arr[j][1]
        elif arr[-1][0] == 4:
            if arr[j][0] == 1:
                result += N - arr[j][1] + arr[-1][1]
            else:
                result += N - arr[-1][1] + M - arr[j][1]
print(result)