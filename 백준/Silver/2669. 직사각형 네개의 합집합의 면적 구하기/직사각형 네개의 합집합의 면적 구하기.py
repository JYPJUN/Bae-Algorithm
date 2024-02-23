list_num = [[0 for i in range(100)] for j in range(100)]

for i in range(4):
    a, b, c, d = map(int, input().split())
    for k in range(a, c):
        for m in range(b, d):
            list_num[k][m] = 1

sum_num = 0

for i in range(len(list_num)):
    sum_num += sum(list_num[i])

print(sum_num)