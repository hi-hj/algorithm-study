import sys
import pprint

def FIND_SHARP(x,y,direction):
    move = -1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<h and 0<=ny<w and grid[nx][ny]=='#':
            move = d
    
    return move

def MOVE_ROBOT(x,y,direction, move):
    global answer
    if direction!= move:
        right_cnt, left_cnt = 0,0
        right_direction, left_direction = direction, direction


        for d in range(1, 4):
            right_cnt +=1
            right_direction = (right_direction+1)%4
            if move == right_direction:
                break
        for d in range(1, 4):
            left_cnt +=1
            left_direction = (left_direction-1)%4
            if move == left_direction:
                break
        print(direction, move, left_cnt, right_cnt)

        if left_cnt < right_cnt:
            answer +='L'
        else:
            answer +='R'

    answer += 'A'
    grid[x+dx[move]][y+dy[move]] = '.'
    grid[x+dx[move]*2][y+dy[move]*2] ='.'

    x = x + dx[move]*2
    y = y + dy[move]*2
    direction = move

    return x,y,direction

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

global dx, dy
dx = [0,1,0,-1]
dy = [1,0,-1,0]


# Step 1: Find Start X,Y,D
start = (-1,-1,-1)
for x in range(h):
    for y in range(w):
        if grid[x][y]=='#':
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<h and 0<=ny<w and grid[nx][ny]=='#':
                    cnt +=1
                    direction = d
            if cnt==1:
                start = (x,y,direction)
                break
    if start !=(-1,-1,-1):
        break

answer = ''

x, y, direction = start
grid[x][y] = '.'


while FIND_SHARP(x,y,direction) !=-1:
    move = FIND_SHARP(x,y,direction)
    # print(move)

    # print(x,y,direction,move)
    x,y,direction = MOVE_ROBOT(x,y,direction,move)


startX, startY, startD = start
print(startX+1, startY+1)
direct_table = {0:'>', 1:'v',2:'<',3:'^'}
print(direct_table[startD])
print(answer)
