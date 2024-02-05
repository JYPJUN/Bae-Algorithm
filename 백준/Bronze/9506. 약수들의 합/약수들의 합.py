while True:
    N = int(input())
    if N == -1:
        break
    lst = []
    for i in range(1, N):
        if N % i == 0:
            lst.append(i)
    
    if sum(lst) == N and N != 0:
        print(N, " = ", " + ".join(str(i) for i in lst), sep="")
    else:
        print(f'{N} is NOT perfect.')