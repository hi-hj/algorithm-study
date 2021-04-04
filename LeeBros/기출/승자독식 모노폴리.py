import sys
import pprint
input = sys.stdin.readline

n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
status = [[0]*n for _ in range(n)]


direction = list(map(int, input().split()))
people = []
for i in range(n):
    for j in range(n):
        if grid[i][j] !=0:
            p = grid[i][j] - 1
            d = direction[p]
            people.append((p,i,j,d))
move_rule = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
pprint.pprint(move_rule)
for p, x,y, d in people:
    print(x,y)
    print(move_rule[p][d-1])


