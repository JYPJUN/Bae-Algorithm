from heapq import heappush, heappop

def dijkstra(start):
    pq = []  # heapq을 쓸 메뉴

    heappush(pq, [0, start])  # 시작지점을 추가
    distance[start] = 0

    while pq:  # pq가 빌 때까지 반복
        dist, now = heappop(pq)

        if distance[now] < dist:  # 방금 꺼낸 거리가 원래 있던거보다 길면 취소
            continue

        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, [new_dist, next_node])

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split()) # N 목표타겟 / E 간선의 개수
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)] * (N+1)
    for _ in range(E):
        s, e, d = map(int, input().split())
        graph[s].append([d, e]) # 거리로 우선순위를 두어 heap할 때 최솟값이 앞으로 가도록 조정

    dijkstra(0)
    print(f'#{tc}', distance[N])