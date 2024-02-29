M, N = map(int, input().split())

arr = [list(input()) for _ in range(M)]
min_cnt = 64
for i in range(M):
    if M - i < 8:
        break
    for j in range(N):
        if N - j < 8:
            break
        cnt = 0
        for p in range(8):
            for q in range(8):
                if p % 2 == 0:
                    if q % 2 == 0:
                        if arr[i+p][j+q] == 'B':
                            cnt += 1
                    else:
                        if arr[i+p][j+q] == 'W':
                            cnt += 1
                elif p % 2 == 1:
                    if q % 2 == 0:
                        if arr[i+p][j+q] == 'W':
                            cnt += 1
                    else:
                        if arr[i+p][j+q] == 'B':
                            cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
        cnt = 0
        for p in range(8):
            for q in range(8):
                if p % 2 == 0:
                    if q % 2 == 0:
                        if arr[i+p][j+q] == 'W':
                            cnt += 1
                    else:
                        if arr[i+p][j+q] == 'B':
                            cnt += 1
                elif p % 2 == 1:
                    if q % 2 == 0:
                        if arr[i+p][j+q] == 'B':
                            cnt += 1
                    else:
                        if arr[i+p][j+q] == 'W':
                            cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
print(min_cnt)