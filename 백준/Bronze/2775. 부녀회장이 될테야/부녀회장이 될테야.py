T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    
    arr_0 = [i for i in range(1, n+1)]
    
    for p in range(k):
        for q in range(1, n):
            arr_0[q] = arr_0[q-1] + arr_0[q]
    
    print(arr_0[-1])