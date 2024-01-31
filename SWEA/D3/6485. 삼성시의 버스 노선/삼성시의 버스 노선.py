case = int(input())
  
for i in range(case):
    lst = [0] * 5000
    N = int(input())
    for j in range(N):
        a, b = map(int, input().split())
        for k in range(a-1, b):
            lst[k] += 1
    P = int(input())
    result_lst = []
    for m in range(1, P+1):
        c = int(input())
        result_lst.append(lst[c-1])
    print(f'#{i+1}', *result_lst)