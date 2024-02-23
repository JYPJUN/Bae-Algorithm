for tc in range(1, 11):
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)] # 이중배열 리스트로 받기
    new_arr = list(map(list, zip(*arr))) # 가로 세로 바꾸기
    # 1은 우측으로, 2는 좌측으로 -> 두개가 부딪치는 상황이 오면 교착
    cnt = 0 # 교착 상태 카운팅
    for i in new_arr:
        now = 0  # 교착상태를 확인할 기준
        for j in i:
            if j == 1: # 오른쪽으로 이동하면서 1을 만나면 기준점 초기화
                now = j
            if now == 1 and j == 2: # now가 1인 상태에서 j가 2라면 교착 발생
                cnt += 1
                now = j # now를 2로 만들어주고 다른 1을 만날 때까지
                        # now를 1상태로 두면 1122222111 일때 뒤의 2가 전부 카운팅됨

    print(f'#{tc}', cnt)