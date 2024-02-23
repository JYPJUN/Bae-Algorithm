import sys

N = int(sys.stdin.readline())

for i in range(N):
    K = list(sys.stdin.readline().rstrip().split('X'))
    number = 0
    for j in K:
        number += sum(i for i in range(1, len(j)+1))
    print(number)