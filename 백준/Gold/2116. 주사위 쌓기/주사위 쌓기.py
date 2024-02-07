import copy
# a-f (0-5) / b-d(1-3) / c-e (2-4)
N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(1, 7): # 반복 숫자
    before_idx = i
    dice_copy = copy.deepcopy(dice)
    for j in range(N): # 다이스의 층 수
        idx = dice_copy[j].index(before_idx) # i가 1면 face_idx 는 2가 나옴
        face_idx = 0
        dice_copy[j][idx] = 0
        if idx == 0:
            face_idx = 5
        elif idx == 1:
            face_idx = 3
        elif idx == 2:
            face_idx = 4
        elif idx == 3:
            face_idx = 1
        elif idx == 4:
            face_idx = 2
        elif idx == 5:
            face_idx = 0
        before_idx = dice_copy[j][face_idx]
        dice_copy[j][face_idx] = 0

    pre_result = 0
    for q in dice_copy:
        pre_result += max(q)

    if pre_result > result:
        result = pre_result

print(result)








