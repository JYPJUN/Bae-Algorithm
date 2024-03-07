from collections import deque

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
arr = deque(arr)

print('<', end='')
while arr:
    arr.rotate(-(K-1))
    print(arr.popleft(), end= '')
    if arr:
        print(', ', end= '')
    else:
        print('>')