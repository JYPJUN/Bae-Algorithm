from collections import deque

N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])

print('<', end='')
while q:
    q.rotate(-(K-1))
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
    else:
        print('>')
