T = int(input())

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우 델타 이동

for tc in range(1, T+1):
    N = int(input())                        # 정사각형 N 의 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 정사각형 배열
    max_cnt = 0                             # max 이동 값을 저장할 변수
    num = N**2                              # 기준점 최솟값을 저장할 변수
    for i in range(N):
        for j in range(N):
            start_number = arr[i][j]        # 이동할 첫 숫자 -> 전체 탐색으로 이동
            change_number = start_number    # 변경할 change_number 변수
            cnt = 0                         # 이동숫자를 카운팅 할 cnt
            a = i                           # 델타 이동을 계속할 좌표 i
            b = j                           # 델타 이동을 계속할 좌표 j
            while True:                     # 이동을 못할 때까지 반복
                for d in dirs:
                    ni = a + d[0]
                    nj = b + d[1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if change_number+1 == arr[ni][nj]: # 다음 숫자와 1차이가 난다면 아래 조건문 실행
                            change_number = arr[ni][nj]    # change_number 를 다음 숫자로 변경
                            a = ni                         # 위치 i 변경
                            b = nj                         # 위치 j 변경
                            break
                else:                                      # break 없이 반복문을 빠져 나왔다면
                    cnt = change_number - start_number+1   # 이동을 못한 것 임으로 else문 실행
                    break                                  # while 반복문 종료

            if max_cnt < cnt:                              # max_cnt 보다 크다면
                max_cnt = cnt
                num = start_number
            elif max_cnt == cnt and num > start_number:    # cnt와 max_cnt가 같고 start_number가 num 보다 작다면 변경
                num = start_number

    print(f'#{tc}', num, max_cnt)