def solution(n, results):
    answer = 0
    arr = [[[], []] for _ in range(n+1)]

    for game in results:
        arr[game[0]][0].append(game[1]) # 내가 이긴 팀은 앞에 추가
        arr[game[1]][1].append(game[0]) # 내가 진 팀은 뒤에 추가

    for i in range(1, n+1):
        for j in arr[i][0]:
            for zero in arr[j][0]:
                if zero not in arr[i][0]:
                    arr[i][0].append(zero)
            # arr[i][0] += arr[j][0]
        for k in arr[i][1]:
            for zero1 in arr[k][1]:
                if zero1 not in arr[i][1]:
                    arr[i][1].append(zero1)
            # arr[i][1] += arr[k][1]

    for p in arr:
        if len(p[0]+p[1]) == n-1:
            answer += 1

    return answer