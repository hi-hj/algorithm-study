import sys
import collections
import math
input = sys.stdin.readline

n,l,r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
# 2. Mix egg
def mix_egg(x, y):
    queue = collections.deque()
    queue.append((x,y))    
    visited[x][y] = True
    egg_list = [(x,y)]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if egg_open[x][y][i]==True and egg_open[nx][ny][(i+2)%4]==True:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    egg_list.append((nx,ny))
    egg_sum = 0
    egg_cnt = 0
    for x, y in egg_list:
        egg_sum += grid[x][y]
        egg_cnt +=1
    egg = int(egg_sum/egg_cnt)
    for x, y in egg_list:
        grid[x][y] = egg
# 1. check status




answer = 0
need_to_mix = True

while need_to_mix==True:
    egg_open = [[[False]*4 for _ in range(n)] for _ in range(n)]
    need_to_mix = False
    for x in range(n):
        for y in range(n):
            now = grid[x][y]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if l<=abs(now-grid[nx][ny])<=r:
                        need_to_mix = True
                        egg_open[x][y][d] = True
                        egg_open[nx][ny][(d+2)%4] = True



    visited = [[False]*n for _ in range(n)]


    
    
    for i in range(n):
        for j in range(n):
            for d in range(4):
                if egg_open[i][j][d] == True and visited[i][j]==False:
                    mix_egg(i,j)
    
    if need_to_mix == True:
        answer +=1
    else:
        print(answer)
        exit()

print(answer)