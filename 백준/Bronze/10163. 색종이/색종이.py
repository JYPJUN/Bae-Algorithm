import sys

N = int(sys.stdin.readline())
arr = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    a, b, x, y = map(int, sys.stdin.readline().split())
    for p in range(b, b+y):
        for q in range(a, a+x):
            arr[p][q] = i

for j in range(1, N+1):
    num = 0
    for n in arr:
        num += n.count(j)
    print(num)