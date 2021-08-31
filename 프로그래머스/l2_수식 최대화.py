import re
import copy
from itertools import permutations


def calc_nums(nums, operators, priority):

    for prior in priority:
 
        while prior in operators:
            idx = operators.index(prior)
            calc = eval(nums[idx] + prior + nums[idx+1])
            nums.pop(idx)
            nums.pop(idx)
            nums.insert(idx, str(calc))
            operators.pop(idx)

            result = calc
    return abs(result)



def solution(expression):
    operators = []
    for e in expression:
        if e in ('*', '+', '-'):
            operators.append(e)
    nums = re.split(r'[-*+]', expression)

    can_make = list(permutations(['*', '-', '+']))

    answer = 0
    for make in can_make:
        copyNum = copy.deepcopy(nums)
        copyOper = copy.deepcopy(operators)
        answer = max(answer, calc_nums(copyNum, copyOper, make))
    return answer
    
    



solution("100-200*300-500+20")
solution("50*6-3*2")






# import copy
# from itertools import permutations
# def solution(expression):
#     answer = []
#     expre = []
#     last_oper = -1
#     for i in range(len(expression)):
#         if i == len(expression)-1:
#             expre.append(expression[last_oper+1:])
#         elif expression[i] in ('-','+','*'):
#             expre.append(expression[last_oper+1:i])
#             expre.append(expression[i])
#             last_oper = i

#     calc = list(permutations(['*','-','+']))



#     for cal in calc:
#         now_expre = copy.deepcopy(expre)

#         for c in cal: # *, - , +
#             i = 0
#             while i < len(now_expre):
#                 if now_expre[i] == c:
#                     tmp = eval(now_expre[i-1] + now_expre[i] + now_expre[i+1])
#                     now_expre = now_expre[:i-1] + [str(tmp)] + now_expre[i+2:]
#                     i= 0
#                 i+=1

#         answer.append(abs(int(now_expre[0])))
#     return max(answer)



# solution("100-200*300-500+20")