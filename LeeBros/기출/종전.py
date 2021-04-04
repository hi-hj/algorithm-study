import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n):
    total += sum(grid[i])



def possible_to_draw(x,y,one,two):
    point = [(x,y)]
    point.append((x-one, y+one))
    point.append((x-one-two, y+one-two))
    point.append((x-two, y-two))
    for x,y in point:
        if 0<=x<n and 0<=y<n: continue
        else: return False
    return True


def get_score(x,y,one,two):
    point = [0,0,0,0,0]
    border = [[False]*n for _ in range(n)]
    for i in range(one+1):
        border[x-i][y+i] = True
        border[x-two-i][y-two+i]= True
    for i in range(two+1):
        border[x-i][y-i] = True
        border[x-one-i][y+one-i] = True

    # 2 era
    for i in range(0, x-two):
        for j in range(0, y+one-two+1):
            if border[i][j] == True:
                break
            point[0] += grid[i][j]
    # 3 era
    for i in range(0, x-one+1):
        for j in range(n-1, y+one-two, -1):
            if border[i][j] == True:
                break
            point[1] += grid[i][j]
    # 4 era
    for i in range(x-two, n):
        for j in range(0, y):
            if border[i][j] == True:
                break
            point[2] += grid[i][j]
    # 5 era
    for i in range(x-one+1, n):
        for j in range(n-1, y-1, -1):
            if border[i][j] == True:
                break
            point[3] += grid[i][j]

    point[4] = total - sum(point)

    return max(point)-min(point)

get_score(3,2,1,1)
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        for one in range(1, n):
            for two in range(1, n):
                if possible_to_draw(i, j, one, two):
                    answer = min(answer, get_score(i,j,one,two))

print(answer)
        

# def calc_land(x,y,one,two):
    


