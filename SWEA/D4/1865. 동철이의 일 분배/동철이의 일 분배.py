# 퍼센테이지 구하는 함수 구현
def percentage(s, arr, pre_percentage):
    global max_percentage
    if s == N: # s 가 끝에 도달했다면 맥스 퍼센트와 비교 후 값을 갱신
        max_percentage = max(max_percentage, pre_percentage)
        return

    if pre_percentage <= max_percentage : # 백 트랙킹, 기존 값보다 작지 않다면
        return

    for i in range(N): # visited 함수로 반복문을 돌려서 재귀 탐색
        if not visited[i]:
            visited[i] = True # 방문 여부 체크
            percentage(s+1, arr, pre_percentage*arr[s][i]) # 재귀 탐색
            visited[i] = False # 방문 여부 초기화

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N 명의 직원과 N명의 일이 있음
    # i 번 직원이 j번 일을 하면 성공할 확률이 Pi(j) 이다.
    lst = [list(map(lambda x : int(x)/100, input().split())) for _ in range(N)] # 직원이 일을 성공할 확률을 이중 배열로 받는다.
    visited = [False] * (N+1) # 방문 여부를 확인할 list
    max_percentage = 0

    percentage(0, lst, 1)

    print(f'#{tc} {max_percentage*100:.6f}') # f 포메팅으로 6자리수까지 표현 7번째 자리가 반올림으로 됨