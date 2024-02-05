number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    N = list(input().split())
    numbers = list(map(str, input().split()))
    cnt = [0] * 10
    result = []

    for i in numbers:
        cnt[number_list.index(i)] += 1

    for j in range(len(number_list)):
        for k in range(cnt[j]):
            result.append(number_list[j])

    print(f'#{tc}')
    print(*result)