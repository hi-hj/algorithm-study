import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


m, n, k = map(int, input().split())
nemo = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            nemo[i][j] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y, x):
    cnt =1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<m and 0<=nx<n and nemo[ny][nx]==0:
            nemo[ny][nx]=1
            cnt +=dfs(ny, nx)
    return cnt

answer = []
nemo_cnt =0
for i in range(m):
    for j in range(n):
        if nemo[i][j]==0:
            nemo[i][j]=1
            answer.append(dfs(i, j))
            nemo_cnt +=1


print(nemo_cnt)

for i in sorted(answer):
    print(i, end=' ')


#print(sorted(answer))