import sys

# 변수 선언 및 입력
n = int(input())
cx, cy = map(int, input().split())
cx, cy = cx-1, cy-1
a = [[0 for _ in range(n)]for _ in range(n)]
maze = [list(input().strip()) for _ in range(n)]
visited = [[[False for _ in range(4)]for _ in range(n)]for _ in range(n)]
cnt = 0
cd = 0


def in_range(x, y):
    return 0<=x<n and 0<=y<n

def wall_exist(x, y):
    return in_range(x, y) and maze[x][y] == '#'


# 조건에 맞춰 움직여봅니다.
def simulate():
    global cx, cy, cd, cnt
    if visited[cx][cy][cd]:
        print(-1)
        sys.exit(0)
    visited[cx][cy][cd] = True
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    nx, ny = cx + dx[cd], cy + dy[cd]
    
    # Step1
    if wall_exist(nx, ny):
        cd = (cd - 1 + 4) % 4
    
    # Step2
    # Case1
    elif not in_range(nx, ny):
        cx, cy = nx, ny
        cnt += 1
    
    # Case 2 & Case 3
    else:
        # 그 방향으로 이동했다 가정헀을 때 바로 오른쪽에 짚을 벽이 있는지 봅니다.
        rx = nx + dx[(cd + 1) % 4]
        ry = ny + dy[(cd + 1) % 4]
        
        # Case2
        if wall_exist(rx, ry):
            cx, cy = nx, ny
            cnt += 1
        
        # Case3
        else:
            cx, cy = rx, ry
            cd = (cd + 1) % 4
            cnt += 2


# for i in range(1, n + 1):
#     given_row = input()
#     for j, elem in enumerate(given_row, start = 1):
#         a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(cx, cy):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(cnt)
















# import sys
# input = sys.stdin.readline
# import collections

# n = int(input())
# x, y = map(int, input().split())
# maze = [list(input().strip()) for _ in range(n)]
# visit =[[[[0] for _ in range(4)] for _ in range(n)] for _ in range(n)]

# def AHEAD_WALL(x, y, d):
#     global ahead_check
#     if d=='R' and y+1<n:
#         if maze[x][y+1]=='#': ahead_check = False
#     elif d=='D' and x+1<n:
#         if maze[x+1][y]=='#': ahead_check = False
#     elif d=='L' and y-1>=0:
#         if maze[x][y-1]=='#': ahead_check = False
#     elif d=='U' and x-1>=0:
#         if maze[x-1][y]=='#': ahead_check = False
#     return


# x, y, d = x-1, y-1, 'R'
# cnt = 0
# still_maze = True



# while still_maze:
#     print(x, y, d)
#     # Turn Right
#     if d=='R': d=='D'
#     elif d=='D': d=='L'
#     elif d=='L': d=='U'
#     elif d=='U': d=='R'

#     # WHILE AHEAD WALL -> Turn Left
#     print(x, y, d)
#     ahead_check = True
#     while(AHEAD_WALL(x, y, d)):
#         if d=='R': d=='U'
#         elif d=='D': d=='R'
#         elif d=='L': d=='D'
#         elif d=='U': d=='L'
    
#     # GO AHEAD
#     if d=='R':
#         if visit[x][y][0]==1:
#             print(-1)
#             sys.exit()
#         visit[x][y][0] = 1
#         cnt +=1
#         x, y = x, y+1
#         if y>n:
#             still_maze = False
    
#     elif d=='D':
#         if visit[x][y][1]==1:
#             print(-1)
#             sys.exit()
#         visit[x][y][1] = 1
#         cnt+=1
#         x, y = x+1, y
#         if x>n:
#             still_maze = False

#     elif d=='L':
#         if visit[x][y][2]==1:
#             print(-1)
#             sys.exit()
#         visit[x][y][2] = 1
#         cnt+=1
#         x, y = x, y-1
#         if y<0:
#             still_maze = False

#     elif d=='U':
#         if visit[x][y][3]==1:
#             print(-1)
#             sys.exit()
#         visit[x][y][3] = 1
#         cnt+=1
#         x, y = x-1, y
#         if x<0:
#             still_maze = False

    
# print(cnt)

    