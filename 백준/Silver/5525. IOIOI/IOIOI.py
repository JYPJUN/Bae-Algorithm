N = int(input())
M = int(input())
S = input()

word = 'IO' * N + 'I'

K = 0
cnt = 0
while K <= len(S):
    if S[K:K+2*N+1] == word:
        cnt += 1
        K += 2
    else:
        K += 1

print(cnt)