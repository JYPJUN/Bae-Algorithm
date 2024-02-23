import sys

arr = list(map(str, sys.stdin.readline().split()))

str1 = ''

for i in arr:
    str1 += i

if str1 == '12345678':
    print('ascending')
elif str1 == '87654321':
    print('descending')
else:
    print('mixed')