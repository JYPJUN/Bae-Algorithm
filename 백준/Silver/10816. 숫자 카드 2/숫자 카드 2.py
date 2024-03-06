from collections import Counter
import sys

N = int(sys.stdin.readline())
arr_N = Counter(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))

for i in arr_M:
    print(arr_N[i], end=' ')