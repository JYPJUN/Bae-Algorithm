N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            number = lst[i]+lst[j]+lst[k]
            if number <= M:
                if result < number:
                    result = number

print(result)