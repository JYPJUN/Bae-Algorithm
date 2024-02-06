N = int(input())
arr_x = []
arr_y = []

for tc in range(1, N+1):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

if N <= 1:
    print(0)
else:
    print((max(arr_y)-min(arr_y)) * (max(arr_x)-min(arr_x)))