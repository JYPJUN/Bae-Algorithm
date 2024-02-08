T = int(input())

for tc in range(1, T+1):
    bracket = list(map(str, input()))
    stack = []
    cnt = 0

    for i in range(len(bracket)):
        if bracket[i] == '(':
            stack.append('(')
        elif bracket[i] == ')':
            if bracket[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    
    print(f'#{tc}', cnt)