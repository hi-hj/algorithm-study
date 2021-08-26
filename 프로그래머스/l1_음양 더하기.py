def solution(absolutes, signs):
    answer = 0
    
    for number, sign in zip(absolutes, signs):
        if sign ==True:
            answer += number
        elif sign ==False:
            answer -= number
    return answer