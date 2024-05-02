lst = [i for i in range(100)]

for j in range(10, 25):
    lst[j] = min(lst[j-1]+1, lst[j-10]+1)

for k in range(25, 100):
    lst[k] = min(lst[k-1]+1, lst[k-10]+1, lst[k-25]+1)

T = int(input())
for tc in range(T):
    N = int(input())
    result = 0

    while N >0:
        result += lst[N%100]
        N //= 100
    print(result)