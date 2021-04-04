import sys
import collections
input = sys.stdin.readline

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


start = []
for _ in range(k):
    r, c = map(int, input().split())
    start.append((r-1, c-1))

stones = [] 
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start, stones):
    cnt = 0
    can_go = [[False]*n for _ in range(n)]
    
    for x, y in start:
        queue = collections.deque()
        queue.append((x, y))
        can_go[x][y] = True
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and (nx, ny) not in stones and can_go[nx][ny]==False:
                    queue.append((nx, ny))
                    can_go[nx][ny] = True
    
    for i in range(n):
        for j in range(n):
            if can_go[i][j] == True: cnt+=1
    return cnt
        

def back_track(cur_idx, cur_list):
    global answer
    if cur_idx == len(stones):
        if len(cur_list) == len(stones)-m:
            answer = max(answer, bfs(start, cur_list))
        return
    
    back_track(cur_idx+1, cur_list)

    cur_list.append(stones[cur_idx])
    back_track(cur_idx+1, cur_list)
    cur_list.pop()

answer = 0
back_track(0, [])

print(answer)

