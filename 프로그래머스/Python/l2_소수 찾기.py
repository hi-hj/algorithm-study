from itertools import permutations



def check_num(number):
    if number == 0 or number ==1:
        return False
    
    for i in range(2, int(number**1/2)+1):
        if number % i ==0:
            return False
    return True

def solution(numbers):
    can_make = []

    for i in range(1, len(numbers)+1):
        can_make += list(permutations(numbers, i))
    #print(can_make)
    can_make = list(set(can_make))
    # print(can_make)
    new_num = set()

    for num in can_make:
        new_num.add(int(''.join(num)))
    # print(new_num)
    
    cnt = 0

    for num in new_num:
        if check_num(num):
            cnt+=1
    return cnt
    

solution("17")
solution("011")



# from itertools import permutations

# def define_num(num):
#     if num ==0 or num ==1:
#         return False
#     for i in range(2, int(num**1/2)+1):
#         if num%i == 0:
#             return False
#     return True

# def solution(numbers):
#     answer = 0
#     can_make =[]
#     for i in range(1, len(numbers)+1):
#         can_make += list(permutations(numbers, i))
#     can_make = list(set(can_make))
#     new_num = set()
#     for num in can_make:
#         new_num.add(int(''.join(num)))
#     print(new_num)
    

#     for num in new_num:
#         if define_num(num):
#             answer+=1
    
#     return answer