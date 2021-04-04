import sys
import copy
import collections
input = sys.stdin.readline

n, q = map(int, input().split())
ice =[list(map(int, input().split())) for _ in range(2**n)]

move = list(map(int, input().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate_ice(n, start):
    if n == 0:
        return
    num = 2**n
    half = 2**(n-1)
    x, y = start

    one = [[0]*half for _ in range(half)]
    two = [[0]*half for _ in range(half)]
    thr = [[0]*half for _ in range(half)]
    fou = [[0]*half for _ in range(half)]
    
    for i in range(half):
        for j in range(half):
            one[i][j] = ice[x+i][y+j]
            two[i][j] = ice[x+i][y+half+j]
            thr[i][j] = ice[x+half+i][y+half+j]
            fou[i][j] = ice[x+half+i][y+j]
    
    for i in range(half):
        for j in range(half):
            # one
            ice[x+i][y+j] = fou[i][j] 
            # two
            ice[x+i][y+half+j] = one[i][j]
            # thr
            ice[x+half+i][y+half+j] = two[i][j]
            # fou
            ice[x+half+i][y+j] = thr[i][j]

def melt():
    global ice
    store_ice = copy.deepcopy(ice)

    for x in range(2**n):
        for y in range(2**n):
            if ice[x][y] == 0: continue
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<2**n and 0<=ny<2**n and ice[nx][ny]>0:
                    cnt +=1
            if cnt >= 3: continue
            else: store_ice[x][y] -=1
    
    ice = store_ice


def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y))
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        cnt +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<2**n and 0<=ny<2**n and ice[nx][ny]!=0 and visited[nx][ny]==False:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt

for level in move:
    for i in range(0, 2**n, 2**level):
        for j in range(0, 2**n, 2**level):
            rotate_ice(level, (i, j))
    melt()


sum_ice = 0

for i in range(2**n):
    for j in range(2**n):
        sum_ice += ice[i][j]
print(sum_ice)

ice_block= []
visited = [[False]*2**n for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if ice[i][j]!=0 and visited[i][j]==False:
            ice_block.append(bfs(i, j))

if not ice_block:
    print(0)
else:
    print(max(ice_block))