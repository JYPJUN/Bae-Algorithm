def postorder(node):
    if node:
        postorder(left[node])
        postorder(right[node])
        if arr[node] == '+':
            arr[node] = int(arr[left[node]]) + int(arr[right[node]])
        elif arr[node] == '-':
            arr[node] = int(arr[left[node]]) - int(arr[right[node]])
        if arr[node] == '/':
            arr[node] = int(arr[left[node]]) // int(arr[right[node]])
        if arr[node] == '*':
            arr[node] = int(arr[left[node]]) * int(arr[right[node]])

for tc in range(1, 11):
    N = int(input())
    arr = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    
    for i in range(N):
        lst = input().split()
        if len(lst) == 4:
            arr[int(lst[0])] = lst[1]
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])
        else:
            arr[int(lst[0])] = lst[1]

    postorder(1)
    print(f'#{tc}', arr[1])