import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

fire = []
wall = []
empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:wall.append((i, j))
        elif grid[i][j] == 2:fire.append((i, j))
        else: empty.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_max_area(add_wall):
    # 방화벽
    new_wall = wall + add_wall

    fired = [[0]*m for _ in range(n)]
    area = n*m
    area -= len(new_wall)

    for x, y in fire:
        queue = collections.deque()
        queue.append((x, y))
        fired[x][y] = 1
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and fired[nx][ny]==0 and (nx, ny) not in new_wall:
                    queue.append((nx, ny))
                    fired[nx][ny] = 1


    for i in range(n):
        for j in range(m):
            if fired[i][j]: area -=1
    return area




def back_track(cur_idx, cur_list):
    global answer
    if cur_idx == len(empty):
        if len(cur_list) == 3:
            answer = max(answer, find_max_area(cur_list))
        return
    if len(cur_list) > 3:
        return
    
    back_track(cur_idx+1, cur_list)

    cur_list.append(empty[cur_idx])
    back_track(cur_idx+1, cur_list)
    cur_list.pop()

answer = 0

back_track(0, [])
print(answer)