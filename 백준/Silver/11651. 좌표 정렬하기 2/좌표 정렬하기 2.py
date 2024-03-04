import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda y: (y[1], y[0]))

for i in arr:
    print(*i)