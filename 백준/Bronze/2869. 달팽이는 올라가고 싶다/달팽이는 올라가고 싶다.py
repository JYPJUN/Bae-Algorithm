A, B, V = map(int, input().split())

turn = A-B

if (V-B) % (A-B) == 0 :
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)