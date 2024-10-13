N = int(input())

if N == 1:
    print(int(input()))  # N이 1일 경우 첫 번째 계단의 값만 출력
else:
    stair = [0] * N
    dp = [0] * N

    for i in range(N):
        stair[i] = int(input())

    dp[0] = stair[0]
    if N > 1:
        dp[1] = stair[0] + stair[1]
    if N > 2:
        dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

    print(dp[N-1])
