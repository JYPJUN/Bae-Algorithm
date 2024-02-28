T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1<<N):
        sub_set = []
        for j in range(N):
            if i & (1<<j):
                sub_set.append(arr[j])
        if K == sum(sub_set):
            cnt += 1
    print(f'#{tc}', cnt)