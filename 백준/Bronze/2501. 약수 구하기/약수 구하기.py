N, K = map(int, input().split())

a_list = []

for i in range(1, N+1):
    if N % i == 0:
        a_list.append(i)

if len(a_list) < K:
    print(0)
else:
    print(a_list[K-1])