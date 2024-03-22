from collections import deque

def bfs(s):
    q = deque([s])
    visited = [0] * 101
    visited[s] = 1
    
    # 가장 깊은 depth의 가장 큰 수
    max_number = s
    # 가장 깊은 depth를 저장
    max_depth = 1
    while q:
        now = q.popleft()
        
        # 갈 수 있는 곳들
        for to in graph[now]:
            # 이미 방문 했다면 pass
            if visited[to]:
                continue
            
            # 현재 방문 = 이전 방문 + 1 번 만에 왔다!
            q.append(to)
            visited[to] = visited[now] + 1
            
            # depth 가 더 깊어졌다면 => max_number 초기화
            # depth 는 같은데 max_number 가 커졌다면 => 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
    return max_number

for tc in range(1, 11):
    N, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i+1]
        graph[s].append(e)

    print(f'#{tc}', bfs(start))