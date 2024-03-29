import sys
k = {1, 2, 3, 4, 5, 6, 7, 8, 9} # 완벽한 배열
def inspection(a): # a 좌표에 가로 세로 3x3을 검사할 함수
    
    # 가로, 세로검사
    d = k-set(arr[a[0]])
    d -= {arr[i][a[1]] for i in range(9)} 

    if len(d) == 0:
        return d
    # 9칸 검사
    a1, b1 = a[0]//3, a[1]//3
    for p in range(3):
        d -= set(arr[a1*3+p][b1*3:b1*3+3])
    return d

def find_complete_sudoku(s): # lst 리스트에 있는 좌표를 돌면서 검사할 함수
    if s == len(lst): # lst 만큼 돌았다면 종료
        for b in arr:
            print(*b)
        exit(0) # 정답 케이스 하나를 찾았다면 이후 루트를 찾지 않고 종료

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