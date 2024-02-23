import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

value = str(A*B*C)

cnt = [0]*10

for i in value:
    cnt[int(i)] += 1

for j in cnt:
    print(j)