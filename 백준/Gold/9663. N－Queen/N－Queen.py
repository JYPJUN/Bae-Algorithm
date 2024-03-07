N = int(input())
arr = [0] * N
cnt = 0
def promising(i):
    for k in range(i):
        if arr[i] == arr[k] or abs(arr[i]-arr[k]) == abs(i-k):
            return False
    return True

def n_queens(i):
    global cnt
    if i == N:
        cnt += 1
        return
    else:
        for j in range(N):
            arr[i] = j
            if promising(i):
                n_queens(i+1)

n_queens(0)

print(cnt)