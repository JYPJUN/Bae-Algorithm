import sys

N, D = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    s, e, length = map(int, sys.stdin.readline().split())
    if e > D or e-s < length:
        continue
    arr.append([s, e, length])

distance = [i for i in range(D+1)]

for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    for s, e, length in arr:
        if i == s:
            distance[e] = min(distance[s]+length, distance[e])

print(distance[D])

