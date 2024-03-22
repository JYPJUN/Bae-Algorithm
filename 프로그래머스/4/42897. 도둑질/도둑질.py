def solution(money):
    N = len(money)

    dp1 = [0] * N
    # 첫번째 집을 꼭 방문한 경우
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, N-1):
        dp1[i] = max(money[i] + dp1[i-2], dp1[i-1])

    # 첫번째을 안방문만 경우
    dp2 = [0] * N
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, N):
        dp2[i] = max(money[i] + dp2[i-2], dp2[i-1])

    return max(max(dp1), max(dp2))

print(solution([1, 2, 3, 1]))