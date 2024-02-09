N, M = map(int, input().split())
lst = list(map(int, input().split()))
arr = []
for i in lst:
    for j in lst:
        for k in lst:
            if i != j and i != k and j != k and i + k + j <= M:
                arr.append((i+k+j))

print(max(arr))