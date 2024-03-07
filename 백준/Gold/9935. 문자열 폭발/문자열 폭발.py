import sys

N = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
K = len(bomb)
stack = []

for i in N:
    stack.append(i)
    if bomb == ''.join(stack[-K:]):
        for k in range(K):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')