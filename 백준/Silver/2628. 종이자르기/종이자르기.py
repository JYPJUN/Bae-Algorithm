garo, sero = map(int, input().split())

garo_lst = [0, garo]
sero_lst = [0, sero]

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        sero_lst.append(b)
    else:
        garo_lst.append(b)

garo_lst.sort()
sero_lst.sort()
max_garo = 0
max_sero = 0

for j in range(len(sero_lst)-1, 0, -1):
    if sero_lst[j] - sero_lst[j-1] > max_sero:
        max_sero = sero_lst[j] - sero_lst[j-1]

for k in range(len(garo_lst)-1, 0, -1):
    if garo_lst[k] - garo_lst[k-1] > max_garo:
        max_garo = garo_lst[k] - garo_lst[k-1]

print(max_sero * max_garo)