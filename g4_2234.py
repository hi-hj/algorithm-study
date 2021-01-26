## 비트 연산자 공부하기


from collections import deque
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if k == 0:
                    if 1 & s[x][y]: continue
                elif k == 1:
                    if 2 & s[x][y]: continue
                elif k == 2:
                    if 4 & s[x][y]: continue
                elif k == 3:
                    if 8 & s[x][y]: continue
                visit[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
    return cnt
n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
visit = [[0] * n for i in range(m)]
result1, result2, result3 = 0, 0, 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            result1 += 1
            result2 = max(result2, bfs(i, j))
for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:
            if num & s[i][j]:
                visit = [[0] * n for k in range(m)]
                s[i][j] -= num
                result3 = max(result3, bfs(i, j))
                s[i][j] += num
            num *= 2
print(result1)
print(result2)
print(result3)