from collections import deque

def bfs(room, sx, sy):
    queue = deque()
    queue.append((sx,sy)) # x,y,dist(거리)
    visited = [[0]*5 for _ in range(5)]
    visited[sx][sy] = 1 # 시작 위치 1로 지정, 이따 1 빼줘야 함
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        if (x,y)!=(sx,sy) and room[x][y] =='P':# 시작점은 아닌데, P가 닿은곳
            return False 
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 내 & 파티션이 없는 곳 & 방문 안 한 곳
            if 0<=nx<5 and 0<=ny<5 and room[nx][ny]!='X' and visited[nx][ny]==0:
                if visited[x][y] < 3:
                    visited[nx][ny] = visited[x][y] +1
                    queue.append((nx,ny))
    return True

def solution(places):
    result = [1]*5

    for i, room in enumerate(places):
        for x in range(5):
            for y in range(5):
                if room[x][y] =='P':
                    if not bfs(room, x,y):
                        result[i] = 0
                        break
    return result





solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])