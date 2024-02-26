T = int(input())

arr = [input() for i in range(T)]

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for j in arr:
    print(j)