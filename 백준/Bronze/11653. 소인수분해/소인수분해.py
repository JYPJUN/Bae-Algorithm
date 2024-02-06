N = int(input())
arr = []

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            arr.append(i)
            N //= i
            break

for j in arr:
    print(j)