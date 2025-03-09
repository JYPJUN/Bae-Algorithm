import sys
import math

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

# 1. Prefix GCD 계산
prefix_gcd = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_gcd[i] = math.gcd(prefix_gcd[i - 1], arr[i - 1])

# 2. Suffix GCD 계산
suffix_gcd = [0] * (N + 2)
for i in range(N, 0, -1):
    suffix_gcd[i] = math.gcd(suffix_gcd[i + 1], arr[i - 1])

# 3. 원소 하나를 제거했을 때의 GCD 계산
max_gcd = 0
minus_num = -1

for i in range(1, N + 1):
    gcd_without_i = math.gcd(prefix_gcd[i - 1], suffix_gcd[i + 1])
    
    if gcd_without_i > max_gcd and arr[i - 1] % gcd_without_i != 0:
        max_gcd = gcd_without_i
        minus_num = arr[i - 1]

# 4. 정답 출력
if max_gcd == 0:
    print(-1)
else:
    print(max_gcd, minus_num)
