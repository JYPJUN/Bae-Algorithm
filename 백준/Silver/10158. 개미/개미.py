w, h = map(int, input().split())
a, b = map(int, input().split())
t = int(input())

if ((t-(w-a))//w) % 2 == 1:
    x = ((t-(w-a)) % w)
else:
    x = w - ((t-(w-a)) % w)

if ((t-(h-b))//h) % 2 == 1:
    y = ((t-(h-b)) % h)
else:
    y = h - ((t-(h-b)) % h)

print(x, y)