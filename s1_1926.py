from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chk = [[0]*M for i in range(N)]
draw = []



for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and chk[i][j]==0:
            q = deque()
            q.append([i, j])
            cnt = 1
            chk[i][j] = 1
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0<=nx<N and 0<=ny<M and arr[nx][ny] and chk[nx][ny]==0:
                            q.append([nx, ny])
                            chk[nx][ny] = 1
                            cnt += 1
            draw.append(cnt)



print(draw)
if len(draw)==0:
    print(len(draw))
    print(0)
else:
    print(len(draw))
    print(max(draw))