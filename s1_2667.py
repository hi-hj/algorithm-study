from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
chk = [[0]*N for _ in range(N)]
apart = []

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and chk[i][j]==0:
            q = deque()
            q.append([i, j])
            cnt = 1
            chk[i][j]=1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] and chk[nx][ny]==0:
                        q.append([nx, ny])
                        cnt +=1
                        chk[nx][ny]=1
            apart.append(cnt)

apart.sort()
print(len(apart))
for i in apart:
    print(i)
