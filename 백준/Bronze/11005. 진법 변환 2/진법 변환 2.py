import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rere(a, b):
    x, y = a // b, a % b
    
    if x == 0:
        return number[y]
    else:
        return rere(x, b) + number[y]

result = rere(a, b)
print(result)