import sys
input = sys.stdin.readline


n = int(input())

work = []
for i in range(n):
    t, p = map(int, input().split())
    work.append((i, t, p))


def can_do(work_set):
    for i in range(0, len(work_set)-1):
        if work_set[i][0] + work_set[i][1] > work_set[i+1][0]:
            return False
    
    for i in range(len(work_set)):
        if work_set[i][0] + work_set[i][1] > n:
            return False

    return True

def calc_sum(work_set):
    sum_list = 0
    for _, _, p in work_set:
        sum_list += p
    return sum_list


answer = 0

def dfs(cur_idx, cur_list):
    global answer

    if cur_idx == n:
        if can_do(cur_list):
            answer = max(answer, calc_sum(cur_list))
        return
    
    dfs(cur_idx+1, cur_list)

    cur_list.append(work[cur_idx])
    dfs(cur_idx+1, cur_list)
    cur_list.pop()

dfs(0, [])
print(answer)