import sys
input = sys.stdin.readline

N = int(input())
arr = []
max_weight = 0

for _ in range(N):
    arr.append(int(input()))
arr.sort()

for i in range(N):
    max_weight = max(arr[i] * (N-i), max_weight)

print(max_weight)