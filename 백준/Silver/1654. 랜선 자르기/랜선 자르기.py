import sys

K, N = map(int, sys.stdin.readline().split())
arr = []

for i in range(K):
    arr.append(int(sys.stdin.readline()))

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for j in arr:
        result += j // mid

    if result >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)