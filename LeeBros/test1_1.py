import sys
from collections import deque

n = int(input())
grid = [input() for _ in range(n)]


nums = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i,j)
        elif grid[i][j] =='E':
            end = (i,j)
        elif grid[i][j] !='.' and grid[i][j]!='#':
            nums.append((int(grid[i][j]), i,j))
nums.append((0, start[0], start[1]))
nums.sort()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# A(x1,y1)-> B(x2,y2) 이동, 최단거리 구하기
def calc_length(x1,y1, x2,y2):
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    
    queue.append((x1, y1,0))
    visited[x1][y1] = 1
    while queue:
        x,y,length = queue.popleft()
        if x == x2 and y == y2:
            return length
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and grid[nx][ny]!='#':
                visited[nx][ny] = 1
                queue.append((nx,ny,length+1))
    return -1

    

# Start 에서 시작 (sx, sy, 0,0) // 0 은 거리, 0은 cnt
a_queue = deque()
a_queue.append((0, start[0], start[1], 0, 0))
check_end = False
answer = sys.maxsize
while a_queue:
    av, ax, ay, al, ac = a_queue.popleft()
    # print(av, ax,ay,al,ac)
    # 3개를 다 채운 경우
    if ac == 3:
        check_end_num = calc_length(ax,ay, end[0], end[1])
        
        if check_end_num !=-1:
            check_end = True
            answer = min(answer, al + calc_length(ax,ay, end[0], end[1]))
        continue
    
    can_go = []
    for num, nx, ny in nums:
        if num > av:
            can_go.append((nx,ny))
    
    for nx, ny in can_go:
        nl = calc_length(ax,ay,nx,ny)
        if nl !=-1:
            a_queue.append((int(grid[nx][ny]), nx, ny, al+nl, ac+1))


if answer == sys.maxsize:
    print(-1)
else:
    print(answer)

    


