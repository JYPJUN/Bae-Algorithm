T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)] # 암호 코드를 문자로 받음
    password_dict = {'0001101': 0, '0011001' : 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    # 암호문을 딕셔너리로 만들어서 해당 문자를 넣으면 바로 숫자로 반환
    lst = ''  # 임시 암호문을 추가할 변수
    for i in arr: # 문자로 받은 암호 코드에서 1이 있다면 해당 열은 암호가 적힌 문자열
        if '1' in i:
            lst = i
            break
    code = ''  # 제대로 작성된 암호문
    code += lst.strip('0') # 앞 뒤 0을 전부 제거
    if len(code) != 56:    # 암호 길이에 맞게 0을 추가 및 코드 반환
        k = 56 - len(code)
        code = '0' * k + code # 앞에 빠진 0의 숫자만큼 추가

    trans_code = []     # 암호를 딕셔너리를 활용하여 숫자로 변환
    for j in range(0, len(code), 7):
        if code[j:j+7] in password_dict: # 딕셔너리 안에 있는 암호라면
            trans_code.append(password_dict[code[j:j+7]]) # trans_code에 암호 추가

    numbers = 0         # 암호의 합
    if len(trans_code) == 8:
        even_num = 0     # 짝수 값들의 합
        odd_num = 0      # 홀수 값들의 합
        for k in range(4):
            odd_num += trans_code[k*2]
            even_num += trans_code[k*2+1]
        if (odd_num*3 + even_num) % 10 == 0: # 홀수*3 + 짝수 의 값이 10의 배수라면
            numbers = sum(trans_code)        # 모든 암호 숫자를 더해서 결과로 반환

    print(f'#{tc}', numbers)