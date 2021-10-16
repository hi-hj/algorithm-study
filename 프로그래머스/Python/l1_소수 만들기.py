from itertools import combinations

def check_prime(number):

    if number <3: # 자연수 3개 더했는데. 2 나오는 경우 없어서 이렇게 함
        return False
    else:
        if number % 2 ==0:
            return False
        for i in range(2, int(number**(1/2))+1):
            if number % i == 0:
                return False
    return True


def solution(nums):
    can_make = list(combinations(nums, 3))
    answer = 0
    for numbers in can_make:

        if check_prime(sum(numbers)):
            answer +=1

    return answer