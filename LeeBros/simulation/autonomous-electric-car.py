import sys
import collections
import copy
input = sys.stdin.readline

n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
car_x, car_y = map(int, input().split())
car_x, car_y = car_x -1, car_y-1
passenger = []
for _ in range(m):
    x_s, y_s, x_e, y_e = map(int, input().split())
    x_s, y_s, x_e, y_e = x_s-1, y_s-1, x_e-1, y_e-1
    passenger.append(((x_s, y_s), (x_e, y_e)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
step = []
visited = []
# 최단 거리 찾기
def bfs(x, y):
    global step
    global visited
    visited = [[False]*n for _ in range(n)]
    step = [[0]*n for _ in range(n)]
    queue = collections.deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and visited[nx][ny]==False:
                step[nx][ny] = step[x][y] +1
                visited[nx][ny] = True
                queue.append((nx, ny))


# can_go = [[False]*n for _ in range(n)]
# can_go[car_x][car_y] = True

# bfs(car_x, car_y)
# print(step)


for i in range(m):
    # 가장가까운 승객 찾기
    bfs(car_x, car_y)
    short = []
    for i, (start, end) in enumerate(passenger):
        x_s, y_s = start
        x_e, y_e = end
        short.append((i, step[x_s][y_s], x_s, y_s, x_e, y_e))
    short.sort(key=lambda x : (x[1], x[2], x[3]))
    # print('car', car_x, car_y)
    # print(grid[car_x][car_y])
    # print(step)
    # print('PERSON:', short)
    # print(c)
    cnt = 0
    for _, find, _, _, _, _ in short:
        if find == 0:
            cnt+=1
    if cnt >1:
        print(-1)
        exit()
    # if grid[car_x][car_y]==1:
    #     print(-1)
    #     exit()

    i, p_length, px_start, py_start, px_end, py_end = short[0]
    if visited[px_start][py_start]==False:
        print(-1)
        exit()
    # CAR -> PASSENGER
    if c>=p_length:
        car_x, car_y = px_start, py_start
        c -= p_length
    else:
        print(-1)
        exit()
    if grid[car_x][car_y]==1:
        print(-1)
        exit()
    # PASSENGER -> TARGET
    bfs(car_x, car_y)
    # print('car:', car_x, car_y)
    # print('target:', px_end, py_end)
    # print(step)
    length = step[px_end][py_end]
    # print(c, p_length)
    if visited[px_end][py_end]==False:
        print(-1)
        exit()
    if c>=length:
        car_x, car_y = px_end, py_end
        c += length
        passenger.remove(((px_start, py_start), (px_end, py_end)))
    else:
        print(-1)
        exit()
    if grid[car_x][car_y]==1:
        print(-1)
        exit()


print(c)




# import sys
# import collections
# import copy
# input = sys.stdin.readline

# n, m, c = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# car_x, car_y = map(int, input().split())
# car_x, car_y = car_x -1, car_y-1
# passenger = []
# for _ in range(m):
#     x_s, y_s, x_e, y_e = map(int, input().split())
#     x_s, y_s, x_e, y_e = x_s-1, y_s-1, x_e-1, y_e-1
#     passenger.append(((x_s, y_s), (x_e, y_e)))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 최단 거리 찾기
# def bfs(x, y, grid):
#     visited = [[False]*n for _ in range(n)]
#     new_grid = copy.deepcopy(grid)
#     queue = collections.deque()
#     queue.append((x, y))
#     new_grid[x][y] = -1
#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0<=nx<n and 0<=ny<n and new_grid[nx][ny]==0 and visited[nx][ny]==False:
#                 new_grid[nx][ny] = new_grid[x][y] -1
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#     return new_grid

# # print(bfs(car_x, car_y, grid))


# for _ in range(m):
#     # 가장가까운 승객 찾기
#     new_grid = bfs(car_x, car_y, grid)
#     short = []
#     for start, end in passenger:
#         x_s, y_s = start
#         x_e, y_e = end
#         short.append((-new_grid[x_s][y_s]-1, x_s, y_s, x_e, y_e))
#     short.sort(key=lambda x : (x[0], x[1], x[2]))

#     # MOVE
#     if grid[car_x][car_y] ==1:
#         print(-1)
#         exit()
#     p_length, px_start, py_start, px_end, py_end = short[0]
#     if p_length < 0:
#         print(-1)
#         exit()
#     # CAR -> PASSENGER
#     if c>=p_length:
#         car_x, car_y = px_start, py_start
#         c -= p_length
#     else:
#         print(-1)
#         exit()


#     # PASSENGER -> TARGET
#     new_grid = bfs(px_start, py_start, grid)
#     length = -new_grid[px_end][py_end]-1
#     if c>=length:
#         car_x, car_y = px_end, py_end
#         c += length
#         passenger.remove(((px_start, py_start), (px_end, py_end)))
#     else:
#         print(-1)
#         exit()


# print(c)