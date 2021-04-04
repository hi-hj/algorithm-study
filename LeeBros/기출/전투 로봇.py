import sys
import collections
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

robot_level = 2
robot_eat = 0
robot_time = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            rx = i
            ry = j
def calc_short(x,y, rx,ry):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = collections.deque()
    queue.append((rx,ry))
    visited = [[0]*n for _ in range(n)]
    visited[rx][ry] = 0
    
    while queue:
        rx, ry = queue.popleft()
        if rx == x and ry == y:
            break
        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            if 0<=nrx<n and 0<=nry<n and can_go[nrx][nry]==True and visited[nrx][nry]==0:
                queue.append((nrx, nry))
                visited[nrx][nry] = visited[rx][ry] + 1

    return visited[x][y]

while True:
    # 1. 갈 곳 찾기
    can_go = [[True]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > robot_level: can_go[i][j] = False
    
    short_go = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] < robot_level and grid[i][j]!=0:
                ml = calc_short(i,j,rx,ry)
                if ml ==0:
                    continue
                else:
                    short_go.append((calc_short(i,j,rx,ry), i, j))

    if not short_go:
        break
    short_go.sort()

    # 2. 이동하기
    
    ml, mx, my = short_go[0]

    robot_time += ml
    grid[rx][ry] = 0
    rx, ry = mx,my
    robot_eat +=1
    if robot_eat == robot_level:
        robot_level +=1
        robot_eat = 0
    
    grid[mx][my] = 0



print(robot_time)

