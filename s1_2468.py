import sys
input = sys.stdin.readline

from collections import deque
def bfs(x, y, height):
    queue = deque()
    queue.append([x, y])
    global rvisit
    rvisit[x][y] = 1

    global dx, dy
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and rmap[nx][ny]>height and rvisit[nx][ny]==0:
                queue.append([nx, ny])
                rvisit[nx][ny] =1
            


n = int(input())
rmap = []
rmax = 0
rvisit = [[0]*n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for r in row:
        rmax = max(r, rmax)
    rmap.append(row)

rlist_height = []
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

for height in range(rmax):
    rcnt = 0
    for i in range(n):
        for j in range(n):
            if rmap[i][j]>height and rvisit[i][j]==0:
                bfs(i, j, height)
                rcnt +=1
                # rlist_height.append(SOMETHING)
    rlist_height.append(rcnt)
    rvisit = [[0]*n for _ in range(n)]

print(max(rlist_height))