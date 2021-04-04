import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]



def not_share(one, two):
    x1, y1, h1, w1 = one
    x2, y2, h2, w2 = two
    
    visited = [[False]*m for _ in range(n)]
    for i in range(x1, x1+h1):
        for j in range(y1, y1+w1):
            visited[i][j] = True
    
    for i in range(x2, x2+h2):
        for j in range(y2, y2+w2):
            if visited[i][j] == True:
                return False
            else:
                continue
    
    return True

def calc_max(one, two):
    x1, y1, h1, w1 = one
    x2, y2, h2, w2 = two
    calc_sum = 0
    for i in range(x1, x1+h1):
        for j in range(y1, y1+w1):
            calc_sum += grid[i][j]
    for i in range(x2, x2+h2):
        for j in range(y2, y2+w2):
            calc_sum += grid[i][j]
    
    return calc_sum
    


answer = -sys.maxsize
for x1 in range(n):
    for y1 in range(m):
        for h1 in range(1, n-x1+1):
            for w1 in range(1, m-y1+1):

                for x2 in range(n):
                    for y2 in range(n):
                        for h2 in range(1, n-x2+1):
                            for w2 in range(1, m-y2+1):
                                if not_share((x1,y1,h1,w1), (x2,y2,h2,w2)):
                                    answer = max(answer, calc_max((x1,y1,h1,w1), (x2,y2,h2,w2)))

print(answer)
