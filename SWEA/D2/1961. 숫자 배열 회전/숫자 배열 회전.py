tc = int(input())

for i in range(1, tc+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst_90 = [[0]*N for _ in range(N)]
    lst_180 = [[0] * N for _ in range(N)]
    lst_270 = [[0] * N for _ in range(N)]

    for m in range(N):
        for n in range(N):
            lst_90[m][n] = lst[N-n-1][m]
            lst_180[m][n] = lst[N-m-1][N-n-1]
            lst_270[m][n] = lst[n][N-m-1]

    result_lst = []
    for idx in range(N):
        result_lst.append(lst_90[idx])
        result_lst.append(lst_180[idx])
        result_lst.append(lst_270[idx])

    print("#{}".format(i))
    for idx, num in enumerate(result_lst):
        if idx % 3 == 0 and idx != 0:
            print()
        numbers = ''.join(map(str, num))
        print(numbers, end = ' ')
    print()