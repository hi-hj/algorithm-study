import sys
#런타임 에러 방지
sys.setrecursionlimit(10000)


T = int(input())

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if (0<=nx<N) and (0<=ny<M):
            if farm[nx][ny]==1:
                farm[nx][ny]=0
                dfs(nx,ny)


for test_case in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        farm[b][a] =1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)

    