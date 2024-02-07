import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
pre_lst = [0]
sum_lst = []
sum_numbers = 0

for i in range(N):
  sum_numbers += lst[i]
  pre_lst.append(sum_numbers)


for j in range(N-K+1):
  sum_lst.append(pre_lst[j+K] - pre_lst[j])

print(max(sum_lst))