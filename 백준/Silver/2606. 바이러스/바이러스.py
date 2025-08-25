import sys
input = sys.stdin.readline

def find(x, info):
    if info[x] != x:
        info[x] = find(info[x], info)
    return info[x]
        
def union(x, y, info):
    root_x = find(x, info)
    root_y = find(y, info)
    
    if root_x == root_y:
        return
    
    if root_x < root_y:
        info[root_y] = root_x
    else:
        info[root_x] = root_y

def solve():
    N = int(input())
    S = int(input())
    
    result = 0
    _info = list(range(N+1))
    
    for _ in range(S):
        a, b = map(int, input().split())
        union(a, b, _info)
    
    for i in range(1, N+1):
        find(i, _info)
    
    result = _info.count(1) - 1
    
    return result

if __name__ == '__main__':
    print(solve())