def solution(a, b):
    answer = 0
    
    for a,b in zip(a,b):
        answer += a*b
    return answer

    # return sum([x*y for x, y in zip(a,b)])