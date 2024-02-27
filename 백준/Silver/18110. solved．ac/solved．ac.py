import sys

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

N = int(sys.stdin.readline())
arr = []
if N == 0:
    print(0)
else:
    for i in range(N):
        arr.append(int(sys.stdin.readline()))
    arr.sort()
    K = round2(N * 0.15)
    sum_number = 0
    if K != 0:
        sum_number += sum(arr[K:-K]) / (len(arr)-2*K)
    else:
        sum_number += sum(arr)/len(arr)

    print(round2(sum_number))
