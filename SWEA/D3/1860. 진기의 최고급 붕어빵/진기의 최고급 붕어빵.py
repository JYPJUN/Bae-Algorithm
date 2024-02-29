T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = ''
    arr.sort()
    for i in range(len(arr)):
        bung = arr[i] // M * K - (len(arr[:i])+1)
        if bung >= 0 :
            result = 'Possible'
        else:
            result = 'Impossible'
            break
    
    print(f'#{tc}', result)