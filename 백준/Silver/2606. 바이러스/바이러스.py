import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)  # 경로 압축
    return parent[x]

def union(x, y, parent):
    rx = find(x, parent)
    ry = find(y, parent)
    if rx == ry:
        return
    # 간단히 번호 작은 쪽에 붙이기 (2606에선 충분)
    if rx < ry:
        parent[ry] = rx
    else:
        parent[rx] = ry

def solve():
    N = int(input())
    S = int(input())

    parent = list(range(N + 1))

    for _ in range(S):
        a, b = map(int, input().split())
        union(a, b, parent)

    root1 = find(1, parent)
    # 1번 컴퓨터를 제외하고, 루트가 root1인 노드 개수
    result = sum(1 for i in range(2, N + 1) if find(i, parent) == root1)
    return result

if __name__ == '__main__':
    print(solve())
