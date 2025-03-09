import sys
input = sys.stdin.readline
N = int(input())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootB] > rank[rootA]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

planets = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []
for dim in range(3):
    planets.sort(key=lambda planet: planet[dim])
    for i in range(N-1):
        cost = abs(planets[i][dim] - planets[i+1][dim])
        edges.append((cost, planets[i][3], planets[i+1][3]))
edges.sort()

parent = [i for i in range(N)]
rank = [0] * N
total_cost = 0
select_edges = 0
for cost, a , b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        total_cost += cost
        select_edges += 1
        if select_edges == N-1:
            break

print(total_cost)