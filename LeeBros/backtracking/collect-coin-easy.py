import sys
import math
input = sys.stdin.readline

n = int(input())

grid = [list(input().strip()) for _ in range(n)]

ans = sys.maxsize
numbers = []
for i in range(n):
    for j in range(n):
        if grid[i][j] not in ('.','S', 'E'):
            numbers.append((int(grid[i][j]), (i, j)))
        elif grid[i][j] =='S':
            start = (i, j)
        elif grid[i][j] =='E':
            end = (i, j)
numbers.sort()

move = []

def calc(move):
    length = abs(start[0]-move[0][0]) + abs(start[1] - move[0][1])
    for i in range(len(move)-1):
        length += abs(move[i][0] - move[i+1][0])
        length += abs(move[i][1] - move[i+1][1])
    length += abs(move[len(move)-1][0] - end[0])
    length += abs(move[len(move)-1][1] - end[1])
    return length

def back_tracking(cur_idx, cnt):
    global ans
    if cnt == 3:
        length = calc(move)
        ans = min(ans, length)
        return
    if cur_idx == len(numbers):
        return
    
    # 동전 선택 X
    back_tracking(cur_idx+1, cnt)

    # 동전 선택 O
    move.append(numbers[cur_idx][1])
    back_tracking(cur_idx+1, cnt+1)
    move.pop()

    
    
back_tracking(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
