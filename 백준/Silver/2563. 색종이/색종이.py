import sys

N = int(sys.stdin.readline().rstrip())

lst = [list(0 for i in range(100)) for j in range(100)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for k in range(10):
        for kk in range(10):
            lst[x+k][y+kk] = 1

total = 0

for m in lst:
    total += sum(m)

print(total)