N = int(input())

arr = [i for i in range(N+1)]
cnt_2 = 0
cnt_5 = 0
for j in arr:
    k = j
    while k != 0:
        if k % 2 == 0:
            k //= 2
            cnt_2 += 1
        elif k % 5 ==0:
            k //= 5
            cnt_5 += 1
        else:
            break

print(min(cnt_2, cnt_5))