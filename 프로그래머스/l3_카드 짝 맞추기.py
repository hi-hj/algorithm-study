import pprint
from collections import defaultdict, deque
from itertools import permutations
import sys

def move(x1,y1,x2,y2, board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((x1,y1,0))
    
    while queue:
        x,y,c = queue.popleft()
        if (x,y) == (x2,y2):
            return c

        for d in range(4): # 4방면
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<4 and 0<=ny<4:
                queue.append((nx, ny,c+1))

        for d in range(4):
            for k in range(2, 4):
                nx = x + dx[d]*k
                ny = y + dy[d]*k
                if 0<=nx<4 and 0<=ny<4 and board[nx][ny]!=0:
                    queue.append((nx,ny, c+1))
                    break
        
def solution(board, r, c):
    x,y = r,c
    grid = board
    pprint.pprint(board)
    cnt = 0
    nums = []
    location = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                location[board[i][j]].append((i,j))
                if board[i][j] not in nums:
                    nums.append(board[i][j])
    print(location, nums)

    can_make = list(permutations(nums, len(nums)))
    print(can_make)
    answer = sys.maxsize

    for numbers in can_make:
        now = 0

        for number in numbers:
            f = location[number][0]
            s = location[number][0]

            
            one = move(x,y,f[0], f[1],board) + move(f[0],f[1],s[0],s[1])
            two = move(x,y,s[0], s[1],board) + move(s[0],s[1],f[0],f[1])
            
            if one > two:
                now += two
                x,y = f[0], f[1]
            else:
                now += one
                x,y = s[0], s[1]
            



    
    # print(move(1,0,2,3, board))

    



solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)