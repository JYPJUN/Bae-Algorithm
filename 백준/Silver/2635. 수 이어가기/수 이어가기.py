N = int(input())

result = 0
result_lst = []
for k in range(1, N+1):
    # 숫자를 담을 리스트
    lst = [N, k]
    # 반복을 돌릴 숫자
    c = N - k
    # 반복문 사용으로 인자 계속 찾기
    while c >= 0:
        c = lst[-2] - lst[-1]
        if c >= 0:
            lst.append(c)

    # 현재 리스트의 길이와 결과 리스트 갱신
    if len(lst) > result:
        result = len(lst)
        result_lst = lst

print(result)
print(*result_lst)