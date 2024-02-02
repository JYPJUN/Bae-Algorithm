T = int(input())

for tc in range(1, T+1):
    # N=상자값, Q 바꿀횟수
    N, Q = map(int, input().split())
	# 상자 숫자 만들기
    box_list = [0 for _ in range(N)]
	# 바꿀 횟수만큼 추가
    for p in range(Q):
        # 바꿀 범위
        L, R = map(int, input().split())
        # index가 0부터 시작하기 때문에 L값에 -1
        for i in range(L-1, R):
            # box 별로 반복되는 p 횟수마다 변경
            box_list[i] = p+1

    print(f'#{tc}', *box_list)