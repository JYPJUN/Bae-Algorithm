def inorder(node): # 중위순회 함수
    global words
    if node != 0:
        inorder(tree[node][1]) # 왼쪽 자식 노드 탐색
        words += tree[node][0] # words에 단어 추가
        inorder(tree[node][2]) # 오른쪽 자식 노드 탐색
    return words

for tc in range(1, 11):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)] # 트리 구조를 받음 [단어, 왼쪽자식노드, 오른쪽자식노드, 부모노드]
    words = ''
    for i in range(1, N+1):
        arr = input().split()
        str1 = arr.pop(1) # 문자는 pop 해서 빼기
        new_arr = [int(n) for n in arr] # arr을 int로 변환하고 리스트로 만들기
        for j in range(1, len(new_arr)): # new_arr의 길이 만큼 반복
            tree[new_arr[0]][j] = new_arr[j] # 자기 자신 노드 자리에 왼쪽자식노드와 오른쪽 자식 노드 추가 1:왼쪽 2 : 오른쪽
            tree[new_arr[j]][3] = new_arr[0] # 자신의 부모 노드 숫자 추가
        tree[i][0] = str1 # 맨 앞의 문자 추가

    root = 0 
    for i in range(1, N+1):
        if tree[i][-1] == 0: # 부모 노드 자리가 0이라면 root
            root = i
            break

    inorder(root)

    print(f'#{tc}', words)