T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    before_stack = []
    for i in range(1, N+1):
        stack = [0] * i
        top = -1
        for j in range(i):
            top += 1
            if len(stack) < 3:
                stack[top] = 1
            elif len(stack) >= 3:
                if top == 0 or top == i-1:
                    stack[top] = 1
                elif j >= 1 or N-1:
                    stack[top] = before_stack[top-1] + before_stack[top]


        print(*stack)
        before_stack = stack