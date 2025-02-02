import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    line = input().strip()
    left_stack = []
    right_stack = []
    
    for char in line:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
    
    print(''.join(left_stack + right_stack[::-1]))
