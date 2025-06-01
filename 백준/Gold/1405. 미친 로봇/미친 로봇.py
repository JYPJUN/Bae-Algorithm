import sys
input = sys.stdin.readline

def dfs(x, y, depth, prob):
    global answer
    
    if depth == N:
        answer += prob
        return

    for i in range(4):
        dx, dy = dirs[i]
        nx, ny = x + dx, y + dy
        
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * probs[i])
            visited[nx][ny] = False

def solve():
    global answer
    answer = 0.0
    
    start_x, start_y = 14, 14
    
    visited[start_x][start_y] = True
    dfs(start_x, start_y, 0, 1.0)
    
    print(f"{answer:.10f}")

if __name__ == '__main__':
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = [[False] * 30 for _ in range(30)]
    N, *probs = map(int, input().split())
    probs = [p / 100 for p in probs]
    solve()