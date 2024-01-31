for i in range(10):
    N = int(input())
    lst = [list(map(int, input().rstrip().split())) for j in range(100)]
 
    max_num = 0
    a, b, c, d = 0, 0, 0, 0 #raw, column, 대각선1, 대각선2
     
    # a 구하기
    for k in range(100):
        if sum(lst[k]) > a:
            a = sum(lst[k])
    # c, d 구하기
    for m in range(100):
        c += lst[m][m]
        d += lst[m][-m-1]
    # b 구하기
    for l in range(100):
        bb = 0
        for n in range(100):
            bb += lst[n][l]
        if bb > b:
            b = bb
 
    max_num = max(a, b, c, d)
 
    print(f'#{i+1}', max_num)