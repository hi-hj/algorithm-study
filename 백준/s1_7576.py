import sys
input = sys.stdin.readline
import collections

m, n = map(int, input().split())
tomato_map = []
queue = collections.deque()
# ★
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j]==1:
            queue.append([i, j])
    tomato_map.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

while queue:
    result +=1
    # ★★
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and tomato_map[ny][nx]==0:
                tomato_map[ny][nx]=1
                queue.append([ny, nx])


for i in range(n):
    for j in range(m):
        if tomato_map[i][j]==0:
            print(-1)
            exit()
print(result-1)