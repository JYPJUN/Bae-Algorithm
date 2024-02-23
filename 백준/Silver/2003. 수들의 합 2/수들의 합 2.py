import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum_number = 0
cnt = 0 

while True:
    if sum_number < M:
        if end == len(arr):
            break
        sum_number += arr[end]
        end += 1
        
    
    if sum_number >= M:
        if sum_number == M:
            cnt += 1
        sum_number -= arr[start]
        start += 1

print(cnt)