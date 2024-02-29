N = int(input())
arr = list(map(int, input().split()))
max_cnt = 1
p = arr[0]

# 오름차순 찾기
cnt = 1
for i in range(1, len(arr)):
    if arr[i] - p >= 0:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    elif arr[i] - p < 0:
        cnt = 1

    p = arr[i]
# 내림차순 찾기
cnt = 1
p = arr[0]
for j in range(1, len(arr)):
    if arr[j] - p <= 0:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    elif arr[j] - p > 0:
        cnt = 1
    p = arr[j]

print(max_cnt)