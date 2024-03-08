import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
lst = [0] * (N+1)

for j in range(N):
    lst[j+1] = arr[j] + lst[j]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lst[b]-lst[a-1])
