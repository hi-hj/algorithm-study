import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

hospital = []
virus = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0 : virus.append((i, j))
        elif grid[i][j] == 2: hospital.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def remove_virus(m_hospital):
    queue = collections.deque()
    visited = [[0]*n for _ in range(n)]
    for x, y in m_hospital:
        visited[x][y] = 1
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안 / 방문한 적 없는 / 벽이 아닌
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and grid[nx][ny]!=1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    for x, y in hospital:
        visited[x][y] = -1
    
    cnt = 0
    catch_virus = []



    for i in range(n):
        for j in range(n):
            if grid[i][j]!=1 and visited[i][j]!=-1 and visited[i][j]!=0:
                catch_virus.append((i, j))
                cnt = max(cnt, visited[i][j])


    if virus == catch_virus:
        return cnt-1
    else:
        return -2




def back_track(cur_idx, cur_list):
    if cur_idx == len(hospital):
        if len(cur_list) == m:
            answer.append(remove_virus(cur_list))

        return
    if len(cur_list) > m:
        return

    back_track(cur_idx+1, cur_list)

    cur_list.append(hospital[cur_idx])
    back_track(cur_idx+1, cur_list)
    cur_list.pop()

answer = []
back_track(0, [])

while -2 in answer:
    answer.remove(-2)

if not answer:
    print(-1)
elif not virus:
    print(0)
else:
    print(min(answer))
