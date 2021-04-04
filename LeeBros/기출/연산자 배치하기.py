import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def compare_oper(oper):
    compare = [0, 0, 0]
    for o in oper:
        if o ==0: compare[0]+=1
        elif o==1: compare[1]+=1
        elif o==2: compare[2]+=1
    
    for i in range(3):
        if compare[i]>operators[i]:
            return False
    return True

def calc_num(oper):
    result = numbers[0]

    for i in range(1, n):
        if oper[i-1] == 0:
            result += numbers[i]
        elif oper[i-1] ==1:
            result -= numbers[i]
        elif oper[i-1] ==2:
            result *= numbers[i]
    
    return result
            

         
            

max_num = -(sys.maxsize)
min_num = sys.maxsize


def dfs(cur_idx, cur_list):
    global max_num, min_num
    if cur_idx == n-1:
        if compare_oper(cur_list):
            max_num = max(max_num, calc_num(cur_list))
            min_num = min(min_num, calc_num(cur_list))
        return
    
    for i in range(3):
        cur_list.append(i)
        dfs(cur_idx+1, cur_list)
        cur_list.pop()
    

dfs(0, [])

print(min_num, end=' ')
print(max_num, end='')