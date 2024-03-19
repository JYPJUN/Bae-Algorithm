def findword(i, j, word):
    global result
    if len(word) == 7:
        result.add(word)
        return

    for d in dirs:
        ni, nj = d[0]+i, d[1]+j
        if 0 <= ni < 4 and 0 <= nj < 4:
            findword(ni, nj, word+arr[ni][nj])

T = int(input())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            findword(i, j, arr[i][j])

    print(f'#{tc}', len(result))