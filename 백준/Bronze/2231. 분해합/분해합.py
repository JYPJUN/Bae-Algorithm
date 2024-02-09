N = int(input())
result = 0

for i in range(1, N):
    arr = []
    a = i
    while True:
        if a == 0:
            break
        arr.append(a%10)
        a //= 10

    if N == i + sum(arr):
        result = i
        break

print(result)