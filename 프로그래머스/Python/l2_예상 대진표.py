def solution(n,a,b):
    answer = 1
    a-=1
    b-=1
    while abs(a-b)>1:
        answer +=1
        a //=2
        b //=2
    print(answer)
    return answer


solution(8,2,3)
# solution(2**20,2,2**20)