T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]* 400
    for i in range(N):
        a, b = map(int, input().split())
        if a % 2 == 0 : a -= 1
        if b % 2 == 0 : b -= 1
        if a > b: a, b = b, a
        for i in range(a, b+1):
            lst[i] += 1
            
    print(f'#{tc}', max(lst))