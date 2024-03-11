while True:
    words = input().rstrip()
    stack = []
    result = 'yes'
    if words == '.':
        break
    for i in range(len(words)):
        if words[i] in '([':
            stack.append(words[i])
        elif words[i] in '])':
            if not stack:
                result = 'no'
                break
            elif words[i] == ']':
                a = stack.pop()
                if a != '[':
                    result = 'no'
                    break
            elif words[i] == ')':
                b = stack.pop()
                if b != '(':
                    result = 'no'
                    break
    if stack:
        result = 'no'
    
    print(result)