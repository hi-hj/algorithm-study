import copy
import sys
n = int(input())
calc = list(input().strip())

oper_list = [i*2+1 for i in range(n//2)]

answer = -sys.maxsize
# 2. 계산하기
def calc_oper(cur_list):
    global answer
    now_calc = copy.deepcopy(calc)

    for i in cur_list:
        calc_sum = int(now_calc[i-1])
        if now_calc[i] == '+':
            calc_sum += int(now_calc[i+1])
        elif now_calc[i] =='-':
            calc_sum -= int(now_calc[i+1])
        elif now_calc[i] =='*':
            calc_sum *= int(now_calc[i+1])
        
        now_calc[i-1] = str(calc_sum)
        now_calc[i], now_calc[i+1] = -1,-1
    
    now_sum = int(now_calc[0])
    for i in range(1, n):
        if now_calc[i] == -1:
            continue
        if not now_calc[i].isdigit():
            if now_calc[i] == '+':
                now_sum += int(now_calc[i+1])
            elif now_calc[i] =='-':
                now_sum -= int(now_calc[i+1])
            elif now_calc[i] =='*':
                now_sum *= int(now_calc[i+1])
    answer = max(answer, now_sum)


# 1 . 연산자 조합 구하기
def get_bracket(cur_idx, cur_list):
    if cur_idx == len(oper_list):
        calc_oper(cur_list)
        return
    
    get_bracket(cur_idx+1, cur_list)
    if not cur_list or oper_list[cur_idx] > cur_list[-1]+2:
        cur_list.append(oper_list[cur_idx])
        get_bracket(cur_idx+1, cur_list)
        cur_list.pop()

get_bracket(0, [])

print(answer)


