def solution(d, budget):
    answer = 0

    d.sort()


    for money in d:
        if budget >= money:
            budget -= money
            answer +=1
        else:
            break
    return answer


solution([1,3,2,5,4], 9)
solution([2,2,3,3], 10 )