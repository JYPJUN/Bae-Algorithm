N = int(input())
arr = [[0]*101 for _ in range(102)]

for i in range(1, N+1):
    a, b, x, y = map(int, input().split())
    for p in range(b, b+y):
        for q in range(a, a+x):
            arr[p][q] = i

for j in range(1, N+1):
    num = 0
    for n in arr:
        num += n.count(j)
    print(num)