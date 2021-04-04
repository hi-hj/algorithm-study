import sys
input = sys.stdin.readline

n = int(input())

box = [list(map(int, input().split())) for _ in range(n)]

result = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[j][n-1-i] = box[i][j]


for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()