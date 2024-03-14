N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y, 0])

for p in range(len(arr)):
    c = 1
    for q in range(len(arr)):
        if p != q:
            if arr[p][1] < arr[q][1] and arr[p][0] < arr[q][0]:
                c += 1
            else:
                continue
    arr[p][2] = c

for n in arr:
    print(n[2], end=' ')