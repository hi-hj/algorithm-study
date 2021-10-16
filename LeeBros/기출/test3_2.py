import collections
import pprint
import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 1. 발생할 수 있는 경우의 수
def dfs(cur_idx, x,y):
    global max_point
    if cur_idx ==3:
        copy_grid = copy.deepcopy(grid)
        pprint.pprint(copy_grid)
        new_grid = move(copy_grid)
        max_point = max(max_point, calc_point(new_grid))
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
            grid[nx][ny] = 1
            dfs(cur_idx+1, nx, ny)
            grid[nx][ny] = 0



# 2. 아래로 쿵
def move(in_grid):

    blocks = in_grid[0:4]
    start, end = -1,-1
    for j in range(m):
        for i in range(4):
            if blocks[i][j] == 1:
                start = j
                break
        if start!=-1:
            break
    
    for j in range(m-1, -1, -1):
        for i in range(4):
            if blocks[i][j]==1:
                end = j
                break
        if end!= -1:
            break
    for i in range(n-1, 0, -1):
        can_go = True
        for j in range(start, end+1):
            if in_grid[i][j] ==1:
                can_go = False
        if can_go:
            for k in range(i, 0, -1):
                in_grid[k][start:end+1] = in_grid[k-1][start:end+1]

    return in_grid




def calc_point(in_grid):
    point = 0
    for i in range(n):
        if sum(in_grid[i]) == m:
            point+=1
    return point

max_point = 0
for i in range(m):
    grid[0][i] = 1
    dfs(0, 0,i)
    grid[0][i] = 0


print(max_point)