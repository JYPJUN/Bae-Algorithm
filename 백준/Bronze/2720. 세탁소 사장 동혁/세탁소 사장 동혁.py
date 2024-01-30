tc = int(input())

for i in range(tc):
    a = int(input())
    # 25 동전 / 10 동전 / 5 동전 / 1동전
    x, y = divmod(a, 25)
    xx, yy = divmod(y, 10)
    xxx, yyy = divmod(yy, 5)
    xxxx, yyyy = divmod(yyy, 1)
    print(x, xx, xxx, xxxx)