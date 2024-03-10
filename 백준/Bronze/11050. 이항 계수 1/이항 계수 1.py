N, K = map(int, input().split())

numbers = 0
def find_binomial_coefficient(N, K):
    global numbers
    if N == K or K == 0:
        numbers += 1
        return
    else:
        find_binomial_coefficient(N-1, K-1)
        find_binomial_coefficient(N-1, K)

find_binomial_coefficient(N, K)

print(numbers)