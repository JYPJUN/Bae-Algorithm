import sys

a = []

for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    a.append(lst)

max_n = 0
row = 0
column = 0
for j in range(9):
    for k in range(9):
        if a[j][k] >= max_n:
            max_n = a[j][k]
            row = j + 1
            column = k + 1

print(max_n)
print(row, column)