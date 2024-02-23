T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    check = str(bin(M))

    if len(check)-2 < N:
        print(f'#{tc}', 'OFF')
    elif '0' in check[::-1][:N]:
        print(f'#{tc}', 'OFF')
    else:
        print(f'#{tc}', 'ON')