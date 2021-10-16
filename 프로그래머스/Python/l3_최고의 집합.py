def solution(n, s):
    if n>s:
        return [-1]
    result = []
    
    for i in range(n):
        a = s//n
        result.append(a)
        s -=a
        n -=1
    return result
