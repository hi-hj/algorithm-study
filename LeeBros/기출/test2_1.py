import sys
from collections import deque


n = int(input())
grid = []
for _ in range(n):
    grid.append(input())
walls = []
start_x, start_y = 0,0

for i in range(n):
    for j in range(n):
        if grid[i][j] =='#':
            walls.append((i,j))
        else:
            start_x, start_y = i,j

answer = 999999
wall_num = len(walls)

def check_wall(cur_walls):
    queue = deque()
    queue.append((start_x, start_y))
    visited = [[0]*n for _ in range(n)]
    visited[start_x][start_y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if grid[nx][ny] =='.' or (nx,ny) in cur_walls:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    sum_num = 0
    for i in range(n):
        sum_num += sum(visited[i])
    
    if n*n == sum_num + wall_num - len(cur_walls):
        return True
    return False


def break_wall(cur_idx, cur_list):
    global answer
    if check_wall(cur_list):
        answer = min(answer, len(cur_list))
    if len(cur_list) > 6:
        return
    if cur_idx == wall_num:
        return
    if len(cur_list) >= answer:
        return

    break_wall(cur_idx+1, cur_list)
    cur_list.append(walls[cur_idx])
    break_wall(cur_idx+1, cur_list)
    cur_list.pop()



break_wall(0, [])

if answer > 6:
    print(-1)
else:
    print(answer)