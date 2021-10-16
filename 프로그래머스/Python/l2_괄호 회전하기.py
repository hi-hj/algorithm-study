def check(string):
    stack = []
    table = {')':'(', ']':'[', '}':'{'}
    
    for char in string:
        if char not in table:
            stack.append(char)
        elif stack and table[char]==stack[-1]:
            stack.pop()
        elif stack and table[char]!=stack.pop():
            return False
        elif not stack and char in table:
            return False
    return len(stack)==0


def solution(s):
    answer = 0 
    for i in range(len(s)):
        if check(s[i:]+ s[:i]):
            answer+=1
    return answer
