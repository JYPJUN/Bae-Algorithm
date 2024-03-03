T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    max_value = 0
    value = 0
    if a == b:
        for i in range(a):
            value += a_arr[i] * b_arr[i]
    elif a > b:
        for p in range(a-b+1):
            for q in range(b):
                value += a_arr[p+q] * b_arr[q]
            if max_value < value:
                max_value = value
            value = 0
    else:
        for p in range(b-a+1):
            for q in range(a):
                value += a_arr[q] * b_arr[p+q]
            if max_value < value:
                max_value = value
            value = 0

    print(f'#{tc}', max_value)