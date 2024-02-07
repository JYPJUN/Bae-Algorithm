for tc in range(1, 11):
    N, password = map(str, input().split())
    lst = [int(i) for i in password]
    stack = [-1] * int(N)
    top = -1

    for i in lst:
        if i not in stack:
            top += 1
            stack[top] = i
        else:
            if stack[top] == i:
                stack[top] = -1
                top -= 1
            else:
                top += 1
                stack[top] = i
    cnt = 0
    for i in stack:
        if i != -1:
            cnt += 1
    f_password = stack[0:cnt]

    print(f'#{tc}', end=' ')
    print(*f_password, sep='')