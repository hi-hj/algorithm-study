import sys
import collections
input = sys.stdin.readline

n, h, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]

hut = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3: hut.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    length = [[0]*n for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and grid[nx][ny]!=1:
                length[nx][ny] = length[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    min_length = sys.maxsize
    for x, y in hut:
        if visited[x][y] == True:
            min_length = min(min_length, length[x][y])
    
    if min_length == sys.maxsize:
        return -1
    return min_length


for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            answer[i][j] = bfs(i, j)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()


