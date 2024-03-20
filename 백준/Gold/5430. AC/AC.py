import sys
from collections import deque

T = int(sys.stdin.readline())
for tc in range(T):
    p = sys.stdin.readline().rstrip().replace('RR', '')  # 명령어
    N = int(sys.stdin.readline())  # 숫자 배열의 수
    arr = sys.stdin.readline().strip("[]\n")
    if arr:
        arr = deque(arr.split(","))
    else:
        arr = deque([])
    check = 1  # 오류인지 아닌지 알려줄 check 항목 / 그리고 R의 좌우 방향 바꾸는거 check
    # check 의 1은 정방향 / 0은 역방향 / -1은 에러!

    for i in p:
        if i == 'R':  # R은 뒤집기
            check = (check+1) % 2
        else:  # D는 배열의 첫 수를 빼기 첫번째 숫자를 빼서 deque를 사용
            if not arr:
                print('error')
                check = -1
                break
            else:
                if check: # 정방향이면 앞에서 빼기
                    arr.popleft()
                else:     # 역방향이면 뒤에서 빼기
                    arr.pop()

    if check != -1: # 오류가 아니면 아래 출력하기
        if len(arr) == 0:  # 비어있으면 빈 리스트 출력
            print('[]')
        else:
            if check: # 정방향 출력이면
                print(f'[{",".join(arr)}]')
            else: # 역방향 출력이면
                arr.reverse()
                print(f'[{",".join(arr)}]')