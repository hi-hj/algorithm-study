import collections
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    visit[x][y] = 1
    v_cnt, k_cnt = 0, 0
    while q:
        x, y = q.popleft()
        if a[x][y] == 'v':
            v_cnt +=1
        elif a[x][y] =='k':
            k_cnt +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if a[nx][ny]!='#' and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
    if v_cnt >= k_cnt:
        k_cnt = 0
    else:
        v_cnt = 0
    return [v_cnt, k_cnt]


m, n = map(int, input().split())
a = [list(input().strip()) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
q = collections.deque()

v, k = 0, 0
for i in range(m):
    for j in range(n):
        if a[i][j] != '#' and not visit[i][j]:
            v_cnt, k_cnt = bfs(i,j)
            v += v_cnt
            k += k_cnt

print(k, v)
