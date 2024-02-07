a, b, c = map(int, input().split())

lst = [a, b, c]

lst.sort()

if lst[-1] >= sum(lst)-max(lst):
    new_max = lst[0] + lst[1] -1
    print(sum(lst) - max(lst) + new_max)
else:
    print(sum(lst))