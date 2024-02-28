import sys

T = int(sys.stdin.readline())
arr = [] # [4 3 6 8 7 5 2 1]

for i in range(T):
  arr.append(int(sys.stdin.readline()))

k = 0 # arr의 index
j = 0 # 다음에 들어갈 수
m = [] # 맨 뒤에 있는 숫자
lst = [] # + - 를 담을 리스트
while True:
  if k != T and arr[k] > j:
    lst.append('+')
    j += 1
    m.append(j)
    
  elif k != T and arr[k] == m[-1]:
    lst.append('-')
    k += 1
    m.pop()
  
  elif not m and j == T:
    break
  
  else:
    lst = ['NO']
    break

for p in lst:
  print(p)