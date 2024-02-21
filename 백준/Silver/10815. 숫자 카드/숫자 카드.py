import sys

N = int(sys.stdin.readline()) # 상근이가 가지고 있는 숫자 카드 개수
n = sorted(list(map(int, sys.stdin.readline().split()))) # 숫자카드 중복 x
M = int(sys.stdin.readline()) # 리스트 M개
m = list(map(int, sys.stdin.readline().split())) # 확인해야할 카드

for i in m:
  low, high = 0, N-1
  exist = False
  while low <= high:
    mid = (low + high) // 2
    if n[mid] > i:
      high = mid -1
    elif n[mid] < i:
      low = mid + 1
    else:
      exist = True
      break
  print(1 if exist else 0, end= ' ')