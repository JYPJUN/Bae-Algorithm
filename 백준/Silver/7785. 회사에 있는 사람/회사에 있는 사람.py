N = int(input())

arr = {}

for i in range(N):
    a, b = input().split()
    if b == 'enter':
        arr[a] = True
    else:
        del arr[a]

print("\n".join(sorted(arr.keys(), reverse=True)))
    