import sys
input = sys.stdin.readline

n, m = map(int, input().split())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

men.sort()
women.sort()
dp = [[0] * (m + 1) for _ in range(n + 1)]

# DP 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        diff = abs(men[i - 1] - women[j - 1])
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + diff
        elif i > j:
            dp[i][j] = min(dp[i - 1][j - 1] + diff, dp[i - 1][j])
        else:  # i < j
            dp[i][j] = min(dp[i - 1][j - 1] + diff, dp[i][j - 1])

print(dp[n][m])
