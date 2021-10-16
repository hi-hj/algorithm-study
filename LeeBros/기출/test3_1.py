import sys
import pprint
import copy
n = int(input())

grid = [list(input().strip()) for _ in range(n)]


for i in range(n):
    for j in range(n):
        if grid[i][j] =='B':
            bx,by = i,j
            grid[i][j] = '.'

bomb = [[0]*n for _ in range(n)]
bomb[bx][by] = 1


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(d, in_bomb):
    out_bomb = [[0]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if in_bomb[x][y] ==1:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]!='#':
                    out_bomb[nx][ny] = 1
                else:
                    return False
    return out_bomb

def big(in_bomb):
    out_bomb = [[0]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if in_bomb[x][y] == 1:
                out_bomb[x][y] =1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]!='#':
                        out_bomb[nx][ny] = 1
                    else:
                        return False
    return out_bomb


answer = 0
def dfs(cur_idx, now_bomb):
    global answer
    if now_bomb:
        answer = max(answer, cur_idx)
    else:
        return
    
    for d in range(4):
        # 이동 (이동이 가능한 경우)
        if move(d, now_bomb):
            new_bomb = move(d, now_bomb)
            # 커지기
            if big(new_bomb):
                new_bomb = big(new_bomb)
                dfs(cur_idx+1, new_bomb)

dfs(0, bomb)

print(answer+1)