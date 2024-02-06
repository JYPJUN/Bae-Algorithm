M = int(input())
N = int(input())

arr = []

for i in range(M, N+1):
    small = []
    for j in range(1, i+1):
        if i % j == 0 and i != 1:
            small.append(j)
    if len(small) == 2:
        arr.append(i)
    else:
        continue

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)