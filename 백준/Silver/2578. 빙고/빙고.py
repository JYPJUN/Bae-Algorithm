import sys
def sol():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if t[k][l] == n[i][j]:
                        check[k] += 1
                        check[l+5] += 1
                        if k+l == 4:
                            check[11] += 1
                        if k==l:
                            check[10] += 1
                        if check.count(5) >= 3:
                            print((i*5+j+1))
                            return

t = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
n = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = [0]* 12
sol()
