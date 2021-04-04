import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = r-1, c-1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y))
    start = grid[x][y]
    can_go = [[False]*n for _ in range(n)]
    can_go[x][y] = False

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]<start and can_go[nx][ny]==False:
                queue.append((nx, ny))
                can_go[nx][ny] = True

    can_go_max = 0
    for i in range(n):
        for j in range(n):
            if can_go[i][j] == True:
                can_go_max = max(can_go_max, grid[i][j])
    
    go_to = (-1, -1)
    for i in range(n):
        for j in range(n):
            if can_go[i][j]==True and grid[i][j] == can_go_max:
                go_to = (i, j)
                break
        if go_to != (-1, -1):
            break
    if go_to ==(-1, -1):
        print(r+1, c+1)
        exit()
    return go_to

for _ in range(k):
    r, c = bfs(r, c)

print(r+1, c+1)
