x, y, w, h = map(int, input().split())

a, b, c, d = w-x, h-y, x, y

print(min(a, b, c, d))