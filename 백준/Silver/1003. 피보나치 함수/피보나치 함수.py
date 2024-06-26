
    

def fibo(N):
    dp = [(0, 0)] * (N+1)
    
    if N == 0:
        return (1, 0)
    elif N == 1:
        return (0, 1)
    
    dp[0] = (1, 0)
    dp[1] = (0, 1)
    
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    
    return dp[N]

T = int(input())

for t in range(T):
    N = int(input())
    
    values = fibo(N)
    
    print(values[0], values[1])