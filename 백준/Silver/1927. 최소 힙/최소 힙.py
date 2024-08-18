import sys
from heapq import heappop, heappush

I = sys.stdin.readline

N = int(I())

heap = []

for i in range(N):
    a = int(I())
    if a == 0 :
        if heap:
            k = heappop(heap)
            print(k)
        else:
            print(0)
    else:
        heappush(heap, a)