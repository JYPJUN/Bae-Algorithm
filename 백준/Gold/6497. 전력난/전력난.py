import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

def solve():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        edges = []
        total_cost = 0
        
        for _ in range(n):
            x, y, z = map(int, input().split())
            edges.append((z, x, y))
            total_cost += z
        
        edges.sort()
        parent = [i for i in range(m)]
        
        mst_cost = 0
        for cost, a, b in edges:
            if union(parent, a, b):
                mst_cost += cost

        print(total_cost - mst_cost)

if __name__ == "__main__":
    solve()