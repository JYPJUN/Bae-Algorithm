import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp_arr = [N+1] * N
dp_arr[0] = 0

for i in range(N-1):
    for j in range(1, arr[i]+1):
        if i + j < N:
            dp_arr[i+j] = min(dp_arr[i]+1, dp_arr[i+j])

if dp_arr[N-1] == N+1:
    print(-1)
else:
    print(dp_arr[N-1])
