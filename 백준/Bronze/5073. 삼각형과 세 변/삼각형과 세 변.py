while True:
    a, b, c = map(int, input().split())
    lst = [a, b, c]

    if a == b == c == 0:
        break

    if max(a, b, c) >= sum(lst)-max(a, b, c):
        print('Invalid')

    elif len(set(lst)) == 1:
        print('Equilateral')

    elif len(set(lst)) == 2:
        print('Isosceles')

    elif len(set(lst)) == 3:
        print('Scalene')