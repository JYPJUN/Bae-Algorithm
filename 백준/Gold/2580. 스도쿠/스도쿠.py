import sys
def inspection(a):
    k = {1, 2, 3, 4, 5, 6, 7, 8, 9} # 완벽한 배열

    # 가로, 세로검사
    k -= set(arr[a[0]])
    for i in range(9):
        k -= {arr[i][a[1]]}
    if len(k) == 0:
        return k
    # 9칸 검사
    a1, b1 = a[0]//3, a[1]//3
    for p in range(3):
        k -= set(arr[a1*3+p][b1*3:b1*3+3])
    return k

def find_complete_sudoku(s):
    if s == len(lst):
        for b in arr:
            print(*b)
        exit(0)

    k = inspection(lst[s]) # 빈칸에 들어갈 수 있는 후보군을 set으로 설정
    if len(k) == 0:
        return

    for i in k:
        arr[lst[s][0]][lst[s][1]] = i
        find_complete_sudoku(s+1)
        arr[lst[s][0]][lst[s][1]] = 0


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
lst = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0] # 빈칸을 넣을 리스트


find_complete_sudoku(0)