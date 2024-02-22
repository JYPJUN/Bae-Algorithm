import sys

N, K = map(int, sys.stdin.readline().split())

arr = [[0,0] for _ in range(6)]

for i in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    arr[Y-1][S] += 1

result = 0
for n in range(len(arr)):
    for m in range(2):
        a, b = divmod(arr[n][m], K)
        result += a
        if b > 0:
            result += 1

print(result)