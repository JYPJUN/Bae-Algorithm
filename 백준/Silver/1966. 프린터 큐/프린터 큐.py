from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque([])
    for idx, value in enumerate(arr):
        q.append([value, idx])

    c = 0
    while True:
        a = q.popleft()
        if q and a[0] >= max(q)[0]:
            c += 1
            if a[1] == M:
                break
        elif len(q) == 0:
            c += 1
            break
        else:
            q.append(a)

    print(c)
