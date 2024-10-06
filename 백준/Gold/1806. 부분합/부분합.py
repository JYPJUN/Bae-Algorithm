import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 초기 값 설정
s, e = 0, 0
current_sum = 0
min_length = float('inf')  # 최소 길이를 무한대로 초기화

while True:
    # 현재 합이 S 이상이면, 길이를 갱신하고 왼쪽 포인터를 이동
    if current_sum >= S:
        min_length = min(min_length, e - s)
        current_sum -= arr[s]
        s += 1
    # 현재 합이 S 미만이면, 오른쪽 포인터를 이동
    elif e == N:  # e가 배열 끝에 도달하면 종료
        break
    else:
        current_sum += arr[e]
        e += 1

# 결과 출력
if min_length == float('inf'):
    print(0)
else:
    print(min_length)
