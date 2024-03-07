M, N = map(int, input().split())

arr = [True] * (N+1)
arr[0] = arr[1] = False

for i in range(2, int(N**0.5)+1):
    if arr[i]:
        for j in range(i**2, N+1, i):
            arr[j] = False

for idx, value in enumerate(arr):
    if value and M <= idx <= N:
        print(idx)