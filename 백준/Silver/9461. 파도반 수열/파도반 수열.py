arr = [0, 1, 1, 1, 2, 2]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    if len(arr)-1 < N:
        while len(arr)-1 != N:
            arr.append(arr[-5]+arr[-1])
        print(arr[N])
    else:
        print(arr[N])