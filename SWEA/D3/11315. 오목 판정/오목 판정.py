T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    result = 'NO' # result의 기본값
    # 한줄 검사 가로
    for i in arr:
        a = set(i.split('.')) # split으로 '.' 기준으로 나누어 연속된 o 찾기
        for j in a:
            if len(j) >= 5: # 문자열 길이가 5 이상이 있으면 연속된 o 찾기 완료
                result = 'YES'
    # 한줄 검사 세로
    new_arr = list(''.join(_).strip('.') for _ in zip(*arr)) # 세로를 가로기준으로 바꾸고 join을 해 문자열로 만듦
    for p in new_arr:
        b = set(p.split('.'))
        for q in b:
            if len(q) >= 5: # 문자열 길이가 5 이상이 있으면 연속된 o 찾기 완료
                result = 'YES'

    # 대각선 검사
    if result != 'YES': # 위에서 연속된 o를 찾기 못했다면
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'o': # 완전 탐색 기준으로 찾기
                    cnt1 = 1
                    cnt2 = 1
                    for k in range(1, 5):
                        if i+k<N and j+k<N and arr[i+k][j+k] == 'o': # 오른쪽 아래 대각선으로 탐색
                            cnt1 += 1
                        if 0<=i-k<N and j+k<N and arr[i-k][j+k] == 'o': # 으른쪾 위 대각선으로 탐색
                            cnt2 += 1
                    if cnt1 >= 5 or cnt2 >= 5: # 둘중 하나라도 5 이상이면
                        result = 'YES'

    print(f'#{tc}', result)