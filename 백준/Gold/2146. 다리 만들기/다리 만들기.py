import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
ireland_num = 2  # 섬 번호 2부터 시작 (1은 원래 육지)
result = float('inf')


def tieLand(i, j):
    """ 섬을 식별하는 BFS """
    q = deque()
    q.append((i, j))
    maps[i][j] = ireland_num
    coast = deque()  # 해안선 좌표 저장

    while q:
        x, y = q.popleft()
        is_coast = False  # 해안선 여부 체크

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == 0:
                    is_coast = True  # 바다와 맞닿아 있으면 해안선
                elif maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = ireland_num

        if is_coast:
            coast.append((x, y))  # 해안선 큐에 추가

    return coast  # 해안선 좌표 반환


# Step 1: 각 섬에 번호 부여 & 해안선 정보 저장
coasts = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            coasts.append(tieLand(i, j))  # 각 섬의 해안선 저장
            ireland_num += 1  # 다음 섬 번호 증가


def checkRoot(coast, land_num):
    """ 해안선에서 출발하여 최단 다리 찾기 (BFS) """
    global result
    q = deque()
    visited = [[False] * N for _ in range(N)]  # 방문 체크 배열

    # 해안선에서 출발
    for x, y in coast:
        q.append((x, y, 0))  # (x, y, 현재 거리)
        visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        # 현재 저장된 최단 거리보다 길면 더 이상 탐색할 필요 없음
        if cnt >= result:
            return

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maps[nx][ny] == 0:
                    # 바다이므로 탐색 계속
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
                elif maps[nx][ny] > 1 and maps[nx][ny] != land_num:
                    # 다른 섬을 만난 경우 최단 거리 갱신
                    result = min(result, cnt)
                    return  # 더 이상 탐색할 필요 없음


# Step 2: 각 섬의 해안선에서 BFS 실행하여 최단 다리 찾기
for idx, coast in enumerate(coasts):
    checkRoot(coast, idx + 2)  # 섬 번호는 2부터 시작했으므로

print(result)  # 가장 짧은 다리 길이 출력
