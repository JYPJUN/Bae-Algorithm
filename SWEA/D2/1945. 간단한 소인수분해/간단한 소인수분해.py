N = int(input())
 
for i in range(N):
    case = int(input())
    lst = [2, 3, 5, 7, 11]
    lst_num = []
    for idx, num in enumerate(lst):
        cnt = 0
        while divmod(case, num)[1] == 0:
            case, res = divmod(case, num)
            cnt += 1
        lst_num += [cnt]
 
    print(f'#{i+1}', *lst_num)