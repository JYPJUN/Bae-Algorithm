def find_set(x): # 부모를 찾는 함수 
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x]) # 경로 압축
    return parents[x]

def union(x, y): # 두 개의 경로를 하나로 묶는 함수 우선 순위 없이 그냥 만나면 엮으면 됨
    x, y = find_set(x), find_set(y)
    if x == y :
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island = [] # x,y 값을 가로로 따로 주기 때문에 모든 섬을 하나의 list로 받아서 만듦
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    m = 0 # 섬의 인덱스를 체크할 변수
    for i in range(N):
        island.append([x_location[i], y_location[i], m]) # 모든 섬의 x 값, y 값, 순번을 같이 리스트에 묶어서 넣기
        m += 1
    E = float(input())
    edges = []
    # 모든 간선을 저장
    for i in range(N):
        for j in range(i+1, N):
            # 코스트와 함께 리스트로 묶어서 간선 정보를 저장
            cost = (island[i][0]-island[j][0])**2 + (island[i][1]-island[j][1])**2
            edges.append([island[i][2], island[j][2], cost])
    edges.sort(key = lambda x : x[2]) # sort에서 람다를 이용해서 코스트를 기준으로 최소 비용이 앞에 오도록 sorting
    parents = [i for i in range(N)] # 각 섬의 부모 노드를 기록하기 위해 (= 연결을 확인하기 위해) 설정

    cnt = 0 # 연결된 수를 셀 카운트 
    sum_value = 0 # 비용 계산할 변수

    for x, y, value in edges: # 모든 간선에 대해서 확인
        if find_set(x) == find_set(y): # 부모가 같으면 싸이클 만들어지기 떄문에 컨티뉴
            continue
        union(x, y) # 싸이클이 안 생기면 묶기
        sum_value += value # 최소 비용 값을 더하기
        cnt += 1 # 연결된 개수 더하기
        
        if cnt == N: # 연결된 개수가 N개 까지 도달하면 for을 종료
            break

    print(f'#{tc}', f'{sum_value*E:.0f}') # f 포메팅으로 0에서 반올림해서 출력