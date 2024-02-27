import sys

T = int(sys.stdin.readline())

for tc in range(T):
    str1 = input().split()

    for i in str1:
        print(i[::-1], end= ' ')