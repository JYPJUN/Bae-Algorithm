T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N 명의 사람, M 초, K 개
    arr = list(map(int, input().split()))
    arr.sort()
    result = 'Possible'
    for i in range(len(arr)):
        m = (arr[i]//M)*K - (len(arr[:i]))
        if m >= 1:
            continue
        else:
            result = 'Impossible'
            break

    print(f'#{tc}', result)