tc = int(input())

for i in range(1, tc+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    # 사각형 내 이동
    dir = [(r, m) for r in range(3) for m in range(3)]

    # 가로행 + 세로행 확인
    row = 0
    column = []
    coll = 0
    square = 0
    for n in range(9):
        row = len(set(lst[n]))
        if row != 9:
            break
    for n in range(9):
        column = []
        for m in range(9):
            column.append(lst[m][n])
        coll = len(set(column))
        if coll != 9:
            break
    # 사각형 확인 0 1 2 3 4 5 6 7 8
    for p in range(0, 9, 3):
        for q in range(0, 9, 3):
            bin_list = []
            for d in dir:
                # 아래로
                dp = p + d[0]
                # 옆으로
                dq = q + d[1]
                bin_list.append(lst[dp][dq])
            square = len(set(bin_list))
            if square != 9:
                break
        else:
            continue
        break
        
    if row + coll + square == 27:
        result = 1
    else:
        result = 0

    print(f'#{i}', result)