import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        num = int(sys.stdin.readline().strip())
        arr.append(num)
    except:
        break

def binary(A):
    if len(A) == 0:
        return

    left, right = [], []
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(A)):
        if A[i] > mid:
            left = A[1:i]
            right = A[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        left = A[1:]
    
    #왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    binary(left)
    binary(right)
    print(mid)

binary(arr)