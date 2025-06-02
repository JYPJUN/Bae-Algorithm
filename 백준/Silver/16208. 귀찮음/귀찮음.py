import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    total = sum(arr)
    point = 0
    
    for p in arr:
        total -= p
        point += p * total
    
    print(point)


if __name__ == "__main__":
    solve()