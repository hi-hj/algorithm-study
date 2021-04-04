import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb = []
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            bomb.append((i, j))


movement = [[(-2,0), (-1,0), (1,0), (2,0)],
            [(-1,0), (0,1), (1,0), (0,-1)],
            [(-1,-1), (-1,1), (1,-1), (1,1)]]


def explosion(bomb, seq):
    exploded = [[0]*n for _ in range(n)]

    for i, (x, y) in enumerate(bomb):
        exploded[x][y] = 1
        for j in range(1, 4):
            if seq[i] == j:
                for dx, dy in movement[j-1]:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<n and 0<=ny<n:
                        exploded[nx][ny]=1
    bomb_num = 0
    for i in range(n):
        bomb_num += sum(exploded[i])
    return bomb_num


max_num = 0
def back_track(cur_idx, cur_list):
    global bomb
    global max_num
    if cur_idx == len(bomb):
        max_num = max(max_num, explosion(bomb, cur_list))
        return
    
    for i in range(1, 4):
        cur_list.append(i)
        back_track(cur_idx+1, cur_list)
        cur_list.pop()

back_track(0, [])

print(max_num)