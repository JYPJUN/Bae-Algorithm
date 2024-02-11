N = int(input())

lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort()

for j in lst:
    print(j)