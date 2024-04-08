from itertools import combinations

# 검사하는 함수
def inspection(array):
    visited = [False] * W
    for i in range(W):
        value = array[0][i] # 검사 배열의 초기값 입력
        cnt = 1
        for j in range(1, D):
            if array[j][i] == value: # value와 같으면 cnt + 1
                cnt += 1
            elif array[j][i] == value:
                cnt += 1
            else:                    # value와 다르면 다른 값으로 바꾸고 cnt 초기화
                value = (value + 1) % 2
                cnt = 1

            if cnt == K:             # cnt 가 K값 과 같아지면 해당 열은 Ture로 바꾸고 다음 열로 넘어감
                visited[i] = True
                break

        if visited[i] == False:      # 검사 중 False로 끝난 열이 있다면 함수 종료
            break

    if False not in visited:         # False가 있으면 성능 검사 실패 아니라면 True로 반환
        return True
    else:
        return False

# 재귀 함수로 약물 투입 경우의 수 구하기
def injection(lst):
    global result

    if inspection(lst): # 초기 검사 시 통과면 함수 바로 빠져나오기
        return

    for k in range(0, D):
        combination_all = []    # 0과 1의 조합으로 순열 만들기
        for n in range(2 ** (k+1)):
            combination = []
            for m in range(k+1):
                bit = (n >> m) & 1      # 비트 연산을 통한 배열 만들기
                combination.append(bit)
            combination_all.append(combination)  # 완성된 배열은 all에 추가

        for comb in combinations([i for i in range(D)], k+1): # 조합으로 바꿀 열을 탐색
            array = [x[:] for x in lst] # 변경할 리스트 복사
            for q in combination_all: # 위에서 만든 순열을 돌면서 변경점 찾기
                cc = 0                # 인덱스 조절용
                for j in comb:        # array 열에 대해서 q의 조합값 대로 넣기
                    array[j] = [q[cc] for _ in range(W)]
                    cc += 1
                if inspection(array):   # 검사 시 통과면 k+1을 반환 후 종료
                    result = k+1
                    return

T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    # D 필름 두께, W 가로크기, K 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]
    result = 0

    injection(arr) # 성능 검사 실행

    print(f'#{tc}', result)