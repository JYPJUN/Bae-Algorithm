import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

pipe1, pipe2, pipe3 = [(0, 1)], [(1, 0)], [(0, 1), (1, 0), (1, 1)]
lst = [pipe1, pipe2, pipe3]

def movepipe(x, y, pipe_index):
    if x == N-1 and y == N-1:
        return 1
    if visited[x][y][pipe_index]:
        return result_board[x][y][pipe_index]

    visited[x][y][pipe_index] = 1
    temp_result = 0
    for i in range(3):
        if (pipe_index == 0 and i == 1) or (pipe_index == 1 and i == 0):
            continue
        for d in lst[i]:
            ni, nj = x + d[0], y + d[1]
            if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == 1:
                break
        else:
            cnt = movepipe(ni, nj, i)
            temp_result += cnt

    result_board[x][y][pipe_index] = temp_result
    return temp_result

visited = [[[0]*3  for _ in range(N)] for _ in range(N)]
result_board = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# 각 위치 및 방향 마다 도달 할 수 있는 경우의 수
result = movepipe(0, 1, 0)

print(result)