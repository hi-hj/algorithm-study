import copy
from itertools import permutations
def solution(expression):
    answer = []
    expre = []
    last_oper = -1
    for i in range(len(expression)):
        if i == len(expression)-1:
            expre.append(expression[last_oper+1:])
        elif expression[i] in ('-','+','*'):
            expre.append(expression[last_oper+1:i])
            expre.append(expression[i])
            last_oper = i
    
    
    calc = list(permutations(['*','-','+']))



    for cal in calc:
        now_expre = copy.deepcopy(expre)

        for c in cal: # *, - , +
            i = 0
            while i < len(now_expre):
                if now_expre[i] == c:
                    tmp = eval(now_expre[i-1] + now_expre[i] + now_expre[i+1])
                    now_expre = now_expre[:i-1] + [str(tmp)] + now_expre[i+2:]
                    i= 0
                i+=1

        answer.append(abs(int(now_expre[0])))
    return max(answer)



solution("100-200*300-500+20")