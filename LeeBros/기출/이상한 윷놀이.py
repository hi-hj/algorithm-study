import sys
import pprint
input = sys.stdin.readline

n, k = map(int, input().split())

# 0 : 흰 / 1 : 빨 / 2 : 파
grid = [list(map(int, input().split())) for _ in range(n)]

horse = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    x,y,d = map(int, input().split())
    horse[x-1][y-1].append((i,d-1))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cnt in range(1, 1001):
    #MOVE
    i = 0
    while i<k:
        for x in range(n):
            for y in range(n):
                if horse[x][y]:
                    for z in range(len(horse[x][y])):
                        num, d = horse[x][y][z]
                        if num ==i:
                            nx = x + dx[d]
                            ny = y + dy[d]

                            # 파랑색
                            # 경계 밖
                            if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==2:
                                if d==0: d=1
                                elif d==1: d=0
                                elif d==2: d=3
                                elif d==3: d=2
                                nx = x + dx[d]
                                ny = y + dy[d]
                                horse[x][y][z] = (num,d)
                                if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==2:
                                    i+=1
                                    break
                                
                            # 흰색
                            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                                horse[nx][ny] += horse[x][y][z:]
                                del horse[x][y][z:]
                                i+=1
                                break
                            # 빨간색
                            elif 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                                print('*****')
                                print(horse[x][y], x,y,z)
                                reverse_horse = reversed(list(horse[x][y][z:]))
                                horse[nx][ny] += reverse_horse
                                del horse[x][y][z:]
                                print(horse[x][y])
                                print(horse[nx][ny])
                                i+=1
                                break
                            

    for i in range(n):
        for j in range(n):
            if len(horse[i][j])>=4:
                print(cnt)
                exit()
                        
pprint.pprint(horse)
print(-1)  