from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque()

for i in range(N):
    t = sys.stdin.readline().split()
    if t[0] == 'push_back':
        arr.append(t[-1])
    elif t[0] == 'push_front':
        arr.appendleft(t[-1])
    elif t[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif t[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif t[0] == 'size':
        print(len(arr))
    elif t[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif t[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif t[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)