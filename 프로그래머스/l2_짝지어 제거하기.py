def solution(s):
    stack = []
    
    for alpha in s:
        if not stack or (stack and stack[-1]!=alpha):
            stack.append(alpha)
        elif stack and stack[-1] == alpha:
            stack.pop()

    if stack:   return 0
    else    :   return 1