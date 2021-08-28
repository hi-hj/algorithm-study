import sys
import pprint
from collections import deque
import copy

N = int(input())

origin_grid =[list(map(int, input().split())) for _ in range(3*N)]
grid = []
for i in range(N):
    imsi = []
    for j in range((3*N)-1, -1, -1):
        imsi.append(origin_grid[j][i])
    grid.append(imsi)
# pprint.pprint(grid)

# Step 1 : Find Can-Erase
def bfs(x, y, num, now_grid):
    global checked
    queue = deque()
    queue.append((x,y))
    checked[x][y] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    erase = [(x,y)]

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<len(now_grid[nx]) and now_grid[nx][ny]==num and checked[nx][ny]==0:
                queue.append((nx, ny))
                checked[nx][ny] = 1
                erase.append((nx, ny))
    
    erase.sort(key = lambda x : (x[0], -x[1]))
    return erase

# Step 2 : Calc Score
def calculator(cars):
    first = len(cars)
    xs = []
    ys = []
    for x,y in cars:
      xs.append(x)
      ys.append(y)
    minX, maxX = min(xs), max(xs)
    minY, maxY = min(ys), max(ys)
    second = (maxX-minX+1) * (maxY-minY+1)

    return first + second

checked = [[0]*N for _ in range(N)]

# Step 3 : DFS : Add Score & Down Car
score = 0
def dfs(now_grid, now_score, count):
    global score
    global checked
    # print("NOW :", now_score, count)
    # pprint.pprint(now_grid)
    if count ==3:
        score = max(score, now_score)
        return
    
    checked = [[0]*N for _ in range(N)]
    can_erase = []
    
    for i in range(N):
        for j in range(N):
            if checked[i][j]==0:
                can_erase.append(bfs(i, j, now_grid[i][j], now_grid))
    

    

    can_erase.sort(key = len, reverse=True)
    for erase in can_erase:
        imsi_grid = copy.deepcopy(now_grid)
        # print("ERASE LIST", erase) 
        for x, y in erase:
            imsi_grid[x].pop(y)
        # pprint.pprint(imsi_grid)


        dfs(imsi_grid, now_score + calculator(erase), count+1)


dfs(grid, 0, 0)

print(score)