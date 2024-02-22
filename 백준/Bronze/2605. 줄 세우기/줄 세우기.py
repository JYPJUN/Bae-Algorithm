import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
arr = []
for j in range(1, N+1):
    arr = arr[:len(arr)-lst[j-1]] + [j] + arr[len(arr)-lst[j-1]:]

print(*arr)