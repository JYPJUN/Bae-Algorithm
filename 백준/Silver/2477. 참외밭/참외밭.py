N = int(input())

height = []
width = []
total = []

for i in range(6):
    P, Q = map(int, input().split())
    if P == 1 or P == 2:
        width.append(Q)
        total.append(Q)
    else:
        height.append(Q)
        total.append(Q)

max_height = max(height)
max_width = max(width)

max_height_idx = total.index(max_height)
max_width_idx = total.index(max_width)

small_height = abs(total[max_height_idx-1] - total[(max_height_idx-5 if max_height_idx == 5 else max_height_idx+1)])
small_width = abs(total[max_width_idx-1] - total[(max_width_idx-5 if max_width_idx == 5 else max_width_idx+1)])

print(N*(max_width*max_height - small_width*small_height))