import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and grid[nx][ny]==0:
                queue.append((nx, ny))
                visited[nx][ny] = True
def check_border(x, y):
    check = False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == True:
            check = True
            break
    
    return check

melt = []

zero_ice = [[0]*m for _ in range(n)]

while zero_ice != grid:
    visited = [[False]*m for _ in range(n)]
    bfs(0, 0)
    melt_cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and check_border(i, j):
                melt_cnt +=1
                grid[i][j] = 0
    melt.append(melt_cnt)


print(len(melt), end=' ')
last = melt.pop()
print(last, end=' ')


