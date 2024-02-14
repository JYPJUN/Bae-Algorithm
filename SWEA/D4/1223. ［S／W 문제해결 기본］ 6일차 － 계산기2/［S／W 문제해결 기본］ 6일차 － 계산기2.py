for tc in range(1, 11):
    N = int(input())
    words = list(input())
    isp = {'+': 1, '*': 2} # 연산자 우선순위 설정
    word = ''

    stack1 = [] # 연산자를 담을 스택
    for i in words:
        if i in '+*': #연산자일 경우 스택에 추가
            if stack1 and isp[i] < isp[stack1[-1]]: # 먼저 들어가있는 연산자보다 우선순위가 낮을 경우
                while stack1: # 스택이 빌 때까지 pop()
                    word += stack1.pop()
            stack1.append(i)
        else: # 숫자일 경우 추가
            word += i
    while stack1: # 나머지 연산자가 전부 빌 때까지 pop()
        word += stack1.pop()

    stack2 = [] # 후위 표기식을 계산할 스택
    for item in word:
        if item in '+*': # 연산자일 경우
            num2 = stack2.pop() # 나오는 숫자의 우선순위를 조심해서 계산할 것
            num1 = stack2.pop()
            if item == '+':
                stack2.append(num1+num2)
            else:
                stack2.append(num1*num2)
        else: # 숫자일 경우 str -> int 로 바꾼 후 삽입
            stack2.append(int(item))

    print(f'#{tc} {stack2.pop()}')