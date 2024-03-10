def find_binomial_coefficient(N, K):
    if N == K or K == 0:
        return 1
    else:
        return find_binomial_coefficient(N-1, K-1) + find_binomial_coefficient(N-1, K)

N, K = map(int, input().split())
print(find_binomial_coefficient(N, K))