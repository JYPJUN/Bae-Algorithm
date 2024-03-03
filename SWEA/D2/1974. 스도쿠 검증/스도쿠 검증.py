T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    sero_arr = list(map(list, zip(*arr)))
    result = 1

    for i in range(len(arr)):
        for p in range(1, 10):
            if p not in arr[i] or p not in sero_arr[i]:
                result = 0
                break
        if result == 0:
            break

    if result != 0:
        for n in range(0, 7, 3):
            for m in range(0, 7, 3):
                check = set()
                for a in range(0, 3):
                    for b in range(0, 3):
                        check.add(arr[n+a][m+b])
                if len(check) != 9:
                    result = 0
                    break
            if result == 0:
                break

    print(f'#{tc}', result)
