N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
def solution(s, pre_sum):
    global cnt
    if s == N:
        if pre_sum == S:
            cnt += 1
        return

    solution(s+1, pre_sum)
    solution(s+1, pre_sum+arr[s])

solution(0, 0)

if S == 0 and cnt == 0:
    print(cnt)
else:
    if S == 0:
        print(cnt-1)
    else:
        print(cnt)
