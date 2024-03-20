import sys
from collections import deque

T = int(sys.stdin.readline())
for tc in range(T):
    p = sys.stdin.readline().rstrip()  # 명령어
    N = int(sys.stdin.readline())  # 숫자 배열의 수
    word = eval(sys.stdin.readline().rstrip()) # json으로 받는게 더 좋아보임.. ex) import json 후 json.loads(input().rstrip())
    check = 1  # 오류인지 아닌지 알려줄 check 항목 / 그리고 R의 좌우 방향 바꾸는거 check
    # check 의 1은 정방향 / 0은 역방향 / -1은 에러!

    arr = deque(word)  # 실행할 수열
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
        if check: # 정방향 출력이면
            if len(arr) == 0: # 비어있으면 빈 리스트 출력
                print('[]')
            else: # 아니라면 원하는 순서대로 출력
                print('[', end='')
                for i in range(len(arr)):
                    if i == len(arr) - 1:  # 마지막 숫자라면
                        print(str(arr[i]) + ']')
                    else:  # 마지막 숫자가 아니라면
                        print(str(arr[i]) + ',', end='')
        else: # 역방향 출력이면
            if len(arr) == 0: # 비어있으면 빈 리스트 출력
                print('[]')
            else:
                print('[', end='')
                for i in range(len(arr)-1, -1, -1):
                    if i == 0:  # 마지막 숫자라면
                        print(str(arr[i]) + ']')
                    else:  # 마지막 숫자가 아니라면
                        print(str(arr[i]) + ',', end='')
