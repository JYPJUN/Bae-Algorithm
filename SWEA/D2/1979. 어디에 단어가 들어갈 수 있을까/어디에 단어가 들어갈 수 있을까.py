T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [''.join(input().split()) for _ in range(N)]
    for i in range(N):
        words = ''
        for j in range(N):
            words += arr[j][i]
        arr.append(words)
    cnt = 0
    for p in arr:
        a = p.split('0')
        for q in a:
            if len(q) == K:
                cnt += 1
    print(f'#{tc}', cnt)