#2178 미로탐색
from collections import deque
#BFS는 deque로 구현해야 더 빠르다고 한다.

#입력
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1 , 0]
dy = [0, 1, 0, -1]
chk = [[0]*m for _ in range(n)]

q = deque()
q.append((0,0))
chk[0][0] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] and not chk[nx][ny]:
            chk[nx][ny] = chk[x][y] + 1
            q.append([nx, ny])

print(chk[n-1][m-1])
