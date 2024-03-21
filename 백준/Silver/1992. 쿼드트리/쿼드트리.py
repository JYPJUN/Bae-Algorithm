import sys

N = int(sys.stdin.readline())

arr = list(sys.stdin.readline().rstrip() for _ in range(N))

def quad_tree(point, N):
    default = arr[point[0]][point[1]]

    check = True
    for i in range(point[0], point[0] + N):
        for j in range(point[1], point[1] + N):
            if arr[i][j] != default:
                check = False
                break
        if check == False:
            break
    if check == True:
        print(str(default), end='')

    else:
        print('(', end='')
        N //= 2
        quad_tree([point[0], point[1]], N)
        quad_tree([point[0], point[1]+N], N)
        quad_tree([point[0]+N, point[1]], N)
        quad_tree([point[0]+N, point[1]+N], N)
        print(')', end='')

quad_tree([0, 0], N)