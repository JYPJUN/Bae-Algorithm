import sys

str1 = sys.stdin.readline().rstrip()
k = sys.stdin.readline().rstrip()

stack = []

for i in str1:
    stack.append(i)
    if i == k[-1]:
        if len(stack) >= len(k) and ''.join(stack[-len(k):]) == k:
            for j in range(len(k)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')