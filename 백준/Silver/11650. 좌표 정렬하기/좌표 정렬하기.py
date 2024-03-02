import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])
arr.sort()

for j in arr:
    print(*j)