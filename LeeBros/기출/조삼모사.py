import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def calc_work(morning):
    night = []
    for i in range(n):
        if i not in morning: night.append(i)
    
    morning_work = 0
    night_work = 0

    for i in morning:
        for j in morning:
            morning_work += grid[i][j]
    for i in night:
        for j in night:
            night_work += grid[i][j]

    return abs(morning_work - night_work)




def dfs(cur_idx, morning):
    global answer
    if cur_idx == n:
        if len(morning) == (n/2):

            answer = min(answer, calc_work(morning))
        return
    
    dfs(cur_idx+1, morning)

    morning.append(cur_idx)
    dfs(cur_idx+1, morning)
    morning.pop()


answer = sys.maxsize
dfs(0, [])
print(answer)
