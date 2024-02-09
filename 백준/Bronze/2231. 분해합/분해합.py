N = int(input())
N_length = N - 9 * len(str(N))

if N_length < 0:
    N_length = 0

for i in range(N_length, N):
    total = i + sum(map(int, str(i)))
    if total == N:
        print(i)
        break
else:
    print(0)