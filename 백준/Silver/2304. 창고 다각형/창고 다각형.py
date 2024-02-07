N=int(input())

lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort()

sum_space = 0

l_lst = [lst[0]]
for j in range(1, N):
    if l_lst[0][1] <= lst[j][1]:
        sum_space += l_lst[0][1] * (lst[j][0]-l_lst[0][0])
        l_lst.pop()
        l_lst.append(lst[j])

r_lst = [lst[N-1]]
for k in range(N-1, -1, -1):
    if l_lst[0][0] <= lst[k][0]:
        if r_lst[0][1] <= lst[k][1]:
            sum_space += r_lst[0][1] * (r_lst[0][0]-lst[k][0])
            r_lst.pop()
            r_lst.append(lst[k])

sum_space += r_lst[0][1]

print(sum_space)