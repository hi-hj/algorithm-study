import sys
from collections import deque

N, T = map(int, input().split())

grid = [[]*N for _ in range(N)]  
for i in range(N):
    for j in range(N):
        grid[i].append(list(map(int, input().split())))

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

signs ={1:(0,1,2), 2:(0,1,3), 3:(1,2,3), 4:(0,2,3),
        5:(0,1),   6:(1,3),   7:(2,3),   8:(0,2),
        9:(0,2),   10:(0,1),  11:(1,3),  12:(2,3)
        }

now = (0,0,0)

queue = deque()
queue.append(now)
visited = set()
visited.add((now))



while queue:
    # print(queue)
    x,y,time = queue.popleft()
    sign = grid[x][y][time]

    for d in signs[sign]:
        # print(d, end=' ') # 0,4,6
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<N and time < T and (nx,ny,(time+1)%4) not in visited:
            queue.append((nx, ny, (time+1)%4))
            visited.add((nx, ny, (time+1)%4))


answer = set()
for x,y,t in visited:
    answer.add((x,y))
print(len(answer))
