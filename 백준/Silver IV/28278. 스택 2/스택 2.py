import sys

I = sys.stdin.readline

N = int(I())

stack = []

for i in range(N):
    K = list(map(int, I().split()))
    if K[0]==1:
        stack.append(K[1])
    elif K[0]==2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif K[0]==3:
        print(len(stack))
    elif K[0]==4:
        if stack:
            print(0)
        else:
            print(1)
    elif K[0]==5:
        if stack:
            print(stack[-1])
        else:
            print(-1)