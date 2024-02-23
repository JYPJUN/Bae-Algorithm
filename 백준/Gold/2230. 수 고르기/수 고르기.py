import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

start = 0
end = 0
min_number = 2000000000

while start <= end and end < N:
    K = abs(arr[start]-arr[end])
    
    if K < M:
        end += 1

    else:
        if K < min_number:
            min_number = K
        elif K == M:
            min_number = K
            break
        start += 1

print(min_number)