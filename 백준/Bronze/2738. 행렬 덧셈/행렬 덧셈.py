import sys

a, b = map(int, input().split())

a_list = [list(map(int, sys.stdin.readline().split())) for i in range(a)]

b_list = [list(map(int, sys.stdin.readline().split())) for j in range(a)]

sum_list = []

for i in range(a):
    middle_list = []
    for j in range(b):
        ab_sum = a_list[i][j] + b_list[i][j]
        middle_list.append(ab_sum)
    sum_list.append(middle_list)
    

for lst in sum_list:
    print(*lst)