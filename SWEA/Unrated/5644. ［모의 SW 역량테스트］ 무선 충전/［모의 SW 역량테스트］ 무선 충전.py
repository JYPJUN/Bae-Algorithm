
def find_max_power(A_position, B_position):
    x1, y1 = A_position
    x2, y2 = B_position
    charge = 0
    pre_charge = 0
    # 모든 Charger에 대해서 max 수치를 찾기 위해 돌림
    if arr[x1][y1] and not arr[x2][y2]:
        for i in arr[x1][y1]:
            pre_charge = i[1]
            if charge < pre_charge:
                charge = pre_charge
    elif not arr[x1][y1] and arr[x2][y2]:
        for j in arr[x2][y2]:
            pre_charge = j[1]
            if charge < pre_charge:
                charge = pre_charge
    else:
        for i in arr[x1][y1]:
            for j in arr[x2][y2]:
                if i[0] == j[0]:
                    pre_charge = i[1]
                else:
                    pre_charge = i[1] + j[1]
                if charge < pre_charge:
                    charge = pre_charge
    return charge


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    # M 사용자 이동횟수
    # A 개의 줄에 걸쳐서 Charger의 정보가 나옴

    # 사용자 이동정보 첫번째 줄이 1번사람 두번째 줄이 2번 사람
    user_move = [list(map(int, input().split())) for _ in range(2)]
    # 0 - 이동 x / 1 - 위로 / 2 - 오른쪽 / 3 - 아래로 / 4 - 왼쪽
    dirs = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


    # Charger 정보를 담을 리스트 구현 (+이동 arr)
    arr = [[[] for _ in range(10)] for z in range(10)]
    AP = 1
    for _ in range(A):
        X, Y, C, P = map(int, input().split())
        for i in range(-C, C+1):
            for j in range(-C + abs(i), C+1 - abs(i)):
                ni, nj = Y + j - 1, X + i - 1
                if 0 <= ni < 10 and 0 <= nj < 10:
                    arr[ni][nj].append((AP, P)) # X가 Y 좌표를 반대로 넣어야 제대로 이동함
        AP += 1
        
    # max charge 값
    max_charge = 0

    # 시작지점
    A_position = [0, 0]
    B_position = [9, 9]
    max_charge += find_max_power(A_position, B_position)

    for i in range(M):
        A_position = [A_position[0]+dirs[user_move[0][i]][0], A_position[1]+dirs[user_move[0][i]][1]]
        B_position = [B_position[0]+dirs[user_move[1][i]][0], B_position[1]+dirs[user_move[1][i]][1]]
        max_charge += find_max_power(A_position, B_position)


    print(f'#{tc}', max_charge)