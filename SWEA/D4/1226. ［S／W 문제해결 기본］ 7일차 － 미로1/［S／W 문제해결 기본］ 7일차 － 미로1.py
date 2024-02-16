from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)] # 미로 이중배열 리스트
    que = deque([[1, 1]]) # deque 로 queue 자료 방식 구현
    result = 0 # 최종 결과 값
    while result == 0 and que: # result 가 0이거나 que가 비지 않을 때 까지 반복
        k = que.popleft() # 탐색할 위치 pop
        arr[k[0]][k[1]] = 1 # 탐색 기준 포인트를 1로 만들어 더 이상 추가 탐색하지 않도록 삭제
        for d in dirs: # 탐색 기준으로 상하좌우 길 찾기
            ni = k[0] + d[0]
            nj = k[1] + d[1]
            if arr[ni][nj] == 0: # 길이라면 좌표 append
                que.append([ni, nj])
            elif arr[ni][nj] == 3: # 출구라면 result를 1로 만들고 break
                result = 1
                break
    print(f'#{tc}', result)