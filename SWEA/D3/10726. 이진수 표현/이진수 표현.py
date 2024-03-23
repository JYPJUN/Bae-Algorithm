T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    if M % 2**(N) == 2**(N)-1:
        print(f'#{tc}', 'ON')
    else:
        print(f'#{tc}', 'OFF')