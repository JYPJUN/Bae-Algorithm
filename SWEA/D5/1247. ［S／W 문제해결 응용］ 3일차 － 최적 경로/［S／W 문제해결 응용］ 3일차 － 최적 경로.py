def housing_system(start, N, pre_sum): # 순열로 집의 순서를 바꿔서 최소 거리 찾는 함수
    global _distance
    if start == N: # start가 N 과 같아졌다면 순열 조합 끝
        # 회사 -> 첫 방문
        pre_sum += (abs(company[0] - customer_house[perms[0]][0]) + abs(company[1] - customer_house[perms[0]][1]))
        # 마지막 방문 -> 집
        pre_sum += (abs(home[0] - customer_house[perms[-1]][0]) + abs(home[1] - customer_house[perms[-1]][1]))
        if _distance > pre_sum: # _distance 보다 pre_sum이 작다면
            _distance = pre_sum
        return

    elif _distance < pre_sum:   # _distance 보다 pre_sum 이 크다면 종료
        return

    for p in range(start, N):
        perms[start], perms[p] = perms[p], perms[start]     # 순열 자리 바꾸기
        # 재귀함수를 통해서 pre_sum을 지속적으로 더해줌 단 start 가 0이면 맨 처음 집 기준으로 index = -1 이 되어서 순열 맨 뒤의 집이랑 빼지니 if else로 방지
        housing_system(start+1, N, pre_sum + ((abs(customer_house[perms[start-1]][0] - customer_house[perms[start]][0]) + abs(customer_house[perms[start-1]][1] - customer_house[perms[start]][1]) if start != 0 else 0)))
        perms[start], perms[p] = perms[p], perms[start]     # 순열 자리 원상복구

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    customer_house = [] # 고객사 집
    for i in range(2, N+2):
        customer_house.append((arr[i*2], arr[i*2+1]))

    company = [arr[0], arr[1]] # 회사 위치
    home = [arr[2], arr[3]] # 집 위치
    perms = [j for j in range(N)]   # 순열을 바꿀 리스트 변수
    _distance = float('inf')    # 거리를 나타낼 변수
    housing_system(0, N, 0)     # 함수 호출 0 : 시작값, N : 고객 집 수, 0 : pre_sum

    print(f'#{tc}', _distance)