import copy

for i in range(10):
    tc = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]
    start_idx = []
    # 시작 지점 찾기
    for idx, num in enumerate(lst[0]):
        if num == 1:
            start_idx.append(idx)


    # 미로 탐색
    # n 세로 / m 가로 idx
    result = 0
    for k in start_idx:
        n, m = 0, k
        test_lst = copy.deepcopy(lst)
        while n < 99:
            if m != 99 and test_lst[n][m+1] == 1:
                    test_lst[n][m] = 0
                    m += 1
            elif m != 0 and test_lst[n][m-1] == 1:
                    test_lst[n][m] = 0
                    m -= 1
            else:
                n += 1
                if n == 99 and test_lst[n][m] == 2:
                    result = k

    print(f'#{i+1}', result)