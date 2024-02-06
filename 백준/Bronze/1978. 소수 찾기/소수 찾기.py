N = int(input())

lst = list(map(int, input().split()))
cnt = 0

for i in lst:
    numbers = []
    for j in range(1, i+1):
        if i % j == 0:
            numbers.append(j)
    if len(numbers) == 2:
        cnt += 1

print(cnt)