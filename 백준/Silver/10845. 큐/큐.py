from _collections import deque
import sys

N = int(sys.stdin.readline())

qq = deque()
for tc in range(N):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'push':
        qq.append(a[1])
    elif a[0] == 'front':
        if qq:
            print(qq[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if qq:
            print(qq[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(qq))
    elif a[0] == 'empty':
        if qq:
            print(0)
        else:
            print(1)
    elif a[0] == 'pop':
        if qq:
            print(qq.popleft())
        else:
            print(-1)
