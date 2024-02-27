import sys

T = int(sys.stdin.readline())

for tc in range(T):
    str1 = sys.stdin.readline().rstrip()

    stack = []
    result = ''
    for i in str1:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'NO'
                break
    if result:
        print(result)
    elif stack:
        print('NO')
    else:
        print('YES')