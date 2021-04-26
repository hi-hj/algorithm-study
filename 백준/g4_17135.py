import sys
import copy
n, m, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 거리 계산
def calc(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
# 1. 궁수가 쏠 놈 찾기
def shoot(x,y,new_grid):
    shoot = False
    sl, sx, sy = sys.maxsize, sys.maxsize, sys.maxsize
    for i in range(n):
        for j in range(m):
            if new_grid[i][j]==1:
                if calc(x,y,i,j) <= d and calc(x,y,i,j) <sl:
                        shoot = True
                        sx, sy = i,j
                        sl = calc(x,y,i,j)
                
                if calc(x,y,i,j) == sl:
                    if j < sy:
                        sx, sy = i,j
    if shoot:
        return (sx, sy)
    else: return False


# 2. 궁수가 쏜 놈 삭제
def delete(shoot_list,new_grid):
    for x,y in shoot_list:
        new_grid[x][y] =0
    return new_grid
    
# 3. 앞으로 당기기
def move(new_grid):
    for i in range(n-2, -1, -1):
        for j in range(m):
            new_grid[i+1][j] = new_grid[i][j]
    for j in range(m):
        new_grid[0][j] = 0
    return new_grid


def simulate(bow_list,new_grid):
    answer = 0

    for i in range(n):
        # print(i)
        shoot_list = []
        for y in bow_list:
            can_shoot = shoot(n,y,new_grid)
            if can_shoot:
                shoot_list.append(can_shoot)
        shoot_list = list(set(shoot_list))
        answer += len(shoot_list)
        new_grid = delete(shoot_list, new_grid)
        new_grid = move(new_grid)
    # print(answer)
    return answer

# 4. 궁수 3명 배치
def dfs(cur_idx, cur_list):
    global max_answer
    if cur_idx == m:
        if len(cur_list)==3:
            # print(cur_list)
            new_grid = copy.deepcopy(grid)
            max_answer = max(max_answer, simulate(cur_list, new_grid))
        return
    if len(cur_list)>3:
        return
    
    dfs(cur_idx+1, cur_list)
    
    cur_list.append(cur_idx)
    dfs(cur_idx+1, cur_list)
    cur_list.pop()

max_answer = 0
dfs(0,[])

print(max_answer)
