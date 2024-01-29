import sys

lst = []

for _ in range(5):
    a = sys.stdin.readline().rstrip()
    lst.append(a)

for i in range(15):
    for j in range(5):
        if i < len(lst[j]):
            print(lst[j][i], end="")