import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        start = 1
        end = 50
        while True:
            mid = (start + end) // 2
            if mid == N:
                print(mid)
                break
            elif mid > N:
                end = mid - 1
                print(mid, end=' ')
            elif mid < N:
                start = mid + 1
                print(mid, end=' ')

