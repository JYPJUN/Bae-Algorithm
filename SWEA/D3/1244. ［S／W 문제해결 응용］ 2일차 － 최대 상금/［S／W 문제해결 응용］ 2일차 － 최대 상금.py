def exchange(x, N):
    global max_m
    if x == N:                                  # x가 N 과 같아질 경우
        cur_m = int(''.join(cost_lst))          # 현재 값을 변수로 할당
        if max_m < cur_m:                       # max 보다 클 경우 max_m을 현재값으로 할당
            max_m = cur_m
        return                                  # x가 N 과 같아지면 함수 종료
    for i in range(len(cost_lst)):              # 변경될 값 i과 j
        for j in range(i+1, len(cost_lst)):
            cost_lst[i], cost_lst[j] = cost_lst[j], cost_lst[i] # i와 j index 숫자의 자리를 교환
            money = int(''.join(cost_lst))                      # 현재 변경된 값의 금액을 확인
            if money not in comp_lst[x]:                        # comp_lst에 없다면 append
                comp_lst[x].append(money)
                exchange(x+1, N)                                # x를 1 증가시키고 재귀함수 호출
            cost_lst[i], cost_lst[j] = cost_lst[j], cost_lst[i] # 값을 원래 자리로 만들고 종료

T = int(input())

for tc in range(1, T+1):
    num, cnt = input().split() # 숫자와 변경횟수를 받음
    N = int(cnt)               # 변경횟수를 int로 변환
    max_m = 0                  # 최댓값을 받을 변수
    cost_lst = list(num)       # 받은 숫자를 리스트로 변환
    comp_lst = [[] for _ in range(N)]   # 변경된 숫자를 넣을 리스트

    exchange(0, N)             # 함수 호출

    print(f'#{tc}', max_m)