import sys
import collections
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

village_cnt = 0
village_people = []

visited = [[False]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y))
    visited[x][y]  = True
    people = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and visited[nx][ny]==False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                people +=1
    
    village_people.append(people)

    return

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and visited[i][j]==False:
            village_cnt +=1
            bfs(i, j)

print(village_cnt)
village_people.sort()
for num in village_people:
    print(num)