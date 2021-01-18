import sys
input = sys.stdin.readline

import collections

n, m , a, b, k = map(int, input().split())
sc_map = [[0]*m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    sc_map[x-1][y-1] = 1

start_end = []
for _ in range(2):
    x, y = map(int, input().split())
    start_end.append([x-1, y-1])


queue = collections.deque()
visited = [[0]*m for _ in range(n)]
answer_list = []

dx= [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Start : x, y, cnt
queue.append([start_end[0][0], start_end[0][1], 0])
visited[start_end[0][0]][start_end[0][1]] =1

while queue:
    y, x, cnt = queue.popleft()
    
    if y==start_end[1][0] and x == start_end[1][1]:
        answer_list.append(cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        hinder = True

        if (0<ny and ny-a<n) and (0<nx and nx+b<m):
            
            for check_y in range(a):
                for check_x in range(b):
                    if sc_map[check_y][check_x]==1:
                        hinder = False
            if hinder==True:
                queue.append([ny, nx, cnt+1])
                visited[ny][nx] = 1

print(answer_list)