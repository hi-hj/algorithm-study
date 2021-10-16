from collections import defaultdict


def divide_profit(man, money):
    global result
    
    # Cetner에서는 연산 종료
    if man =='-':
        return
    
    # 1. 이익 추가
    result[man] += money
    
    # 2. 1/10 계산하기
    divide_money = money//10
    if money//10 >=1:
        result[man] -= divide_money
        divide_profit(matching[man], divide_money)

    
    

def solution(enroll, referral, seller, amount):
    global matching
    global result
    matching = defaultdict()
    result = defaultdict(int)
    
    # Default Dict 할당
    for i in range(len(enroll)):
        up = referral[i]
        down = enroll[i]  
        matching[down] = up
        result[down] = 0
    
    # 순서대로 연산 실행
    for i in range(len(seller)):
        man = seller[i]
        money = amount[i]*100
        divide_profit(man, money)
    
    answer = list(result.values())
    return answer


