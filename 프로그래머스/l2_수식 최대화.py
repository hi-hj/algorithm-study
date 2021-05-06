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
    print(expre)
    print(calc)


    for cal in calc:
        now_expre = copy.deepcopy(expre)
        print(cal)
        for c in cal: # *, - , +
            i = 0
            while i < len(now_expre):
                if now_expre[i] == c:
                    print(i, now_expre)
                    tmp = eval(now_expre[i-1] + now_expre[i] + now_expre[i+1])
                    now_expre = now_expre[:i-1] + [str(tmp)] + now_expre[i+2:]
                    i= 0
                i+=1
        print(now_expre)
        answer.append(abs(int(now_expre[0])))

    print(answer)
            # for i, val in enumerate(now_expre):
            #     if val == c:
            #         print(now_expre)
            #         print(i, val, c)
            #         tmp = eval(now_expre[i-1]+now_expre[i]+now_expre[i+1])
                    
            #         if len(now_expre)==3:
            #             answer.append(tmp)
            #         else:
            #             now_expre = now_expre[:i-1] +[str(tmp)] + now_expre[i+2:]
            #         print(now_expre)
                    



    
    
    


solution("100-200*300-500+20")