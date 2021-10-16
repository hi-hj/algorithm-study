dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 이전 방향 d : 1을 만나면 (d+1)%4
# 이전 방향 d : 2를 만나면 (d-1)%4

import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for  _ in range(n)]
bids = list(map(int, input().split()))

one = set()
two = set()
thr = []

for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            one.add((i,j))
        elif grid[i][j]==2:
            two.add((i,j))
        elif grid[i][j]==3:
            thr.append((i,j))

# 1. 구슬 세팅
for i in range(n):
    # 위
    if bids[i] == 1:
        board[0][i].append(0)
    # 오른쪽
    if bids[i+n] == 1:
        board[i][n-1].append(3)
    # 아래쪽
    if bids[i+2*n] ==1:
        board[n-1][n-1-i].append(1)
    # 왼쪽
    if bids[i+3*n] ==1:
        board[n-1-i][0].append(2)

# Start : 3으로 만드는 경우의 수
def set_slash(cur_idx, one_list, two_list):
    if cur_idx == len(thr):
        print(one_list, two_list)
        return
    # 3 --> 0
    set_slash(cur_idx+1, one_list, two_list)
    # 3 --> 1
    one_list.append(thr[cur_idx])
    set_slash(cur_idx+1, one_list, two_list)
    one_list.pop()
    # 3 --> 2
    two_list.append(thr[cur_idx])
    set_slash(cur_idx+1, one_list, two_list)
    two_list.pop()

# MOVE
def move():
    global board
    print('board', board)
    new_board = [[[] for _ in range(n)] for  _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(board[i][j])==1:
                for d in board[i][j]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        # 0인 경우
                        if grid[nx][ny] == 0:
                            new_board[nx][ny].append(d)
                        # 1인 경우
                        if grid[nx][ny] ==1:
                            new_board[nx][ny].append((d+1)%4)
                        # 2인 경우
                        if grid[nx][ny] ==2:
                            new_board[nx][ny].append((d-1)%4)
    board = new_board
# CRASH

move()
print(board)
