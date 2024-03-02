import sys

N = int(sys.stdin.readline())
arr_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))

arr_N.sort()

for i in arr_M:
    result = 0
    first = 0
    end = N - 1
    while first <= end:
        mid = (first + end) // 2
        if arr_N[mid] == i:
            result = 1
            break
        elif arr_N[mid] < i:
            first = mid + 1
        elif arr_N[mid] > i:
            end = mid - 1
    print(result)