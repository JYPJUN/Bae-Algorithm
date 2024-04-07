from collections import deque

dirs = [(0,1), (1,0), (-1,0), (0,-1)]
# 벽돌을 아래로 내리는 함수
def down_block(x, y, lst):
    for i in range(W):
        for j in range(H-1, -1, -1):
            if lst[j][i] == 0 :
                for a in range(j-1, -1, -1):
                    if lst[a][i] != 0:
                        lst[j][i] = lst[a][i]
                        lst[a][i] = 0
                        break
                else:
                    break
    return

# 구슬을 다 쓸 때까지 재귀함수 실행
def break_bricks(s, lst):
    global min_cnt
    if s == N:
        cnt = W*H
        for m in range(H):
            cnt -= lst[m].count(0)
        min_cnt = min(cnt, min_cnt)
        return

    for i in range(W):
        for j in range(H):
            next_block = [x[:] for x in lst]
            if next_block[j][i] == 1:
                next_block[j][i] = 0
                break
            elif next_block[j][i] not in (0, 1):
                q = deque([(j, i)])
                while q:
                    a, b = q.popleft()
                    k_num = next_block[a][b]
                    next_block[a][b] = 0
                    for k in range(1, k_num):
                        for d in dirs:
                            ni, nj = a+d[0]*k, b+d[1]*k
                            if 0 <= ni < H and 0 <= nj < W:
                                if next_block[ni][nj] in (0, 1):
                                    next_block[ni][nj] = 0
                                else:
                                    q.append((ni, nj))
                # 블록을 제거했다면 내리는 작업 실행
                down_block(0, 0, next_block)
                break
            # 재귀함수를 타서 다음 구슬로 이동
        break_bricks(s+1, next_block)

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    # 구슬의 수
    # W 가로
    # H 세로
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = W * H

    break_bricks(0, arr)

    print(f'#{tc}', min_cnt)