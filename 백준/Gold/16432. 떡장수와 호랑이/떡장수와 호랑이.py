import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve():
    N = int(input())
    dduck = [[] for _ in range(N)]
    
    for i in range(N):
        a, *arr = list(map(int, input().split()))
        dduck[i] = arr
    
    dp = [[-1] * 11 for _ in range(N)]
    path = [[-1] * 11 for _ in range(N)]
    
    def dfs(day, prev):
        if day == N:
            return True
        
        if dp[day][prev] != -1:
            return dp[day][prev] == 1
        
        for val in dduck[day]:
            if val == prev:
                continue
            if dfs(day+1, val):
                dp[day][prev] = 1
                path[day][prev] = val
                return True
        
        dp[day][prev] = 0
        return False
    
    if dfs(0, 0):
        result = []
        prev = 0
        for day in range(N):
            val = path[day][prev]
            result.append(val)
            prev = val
        for r in result:
            print(r)
    else:
        print(-1)
    


if __name__ == "__main__":
    solve()