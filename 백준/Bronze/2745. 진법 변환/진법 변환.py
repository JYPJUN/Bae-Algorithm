import sys

a, b = sys.stdin.readline().rstrip().split()
b = int(b)
a = a[::-1]

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum_num = 0

for i, n in enumerate(a):
    sum_num += number.index(n) * (b**i)

print(sum_num)