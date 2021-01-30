from collections import deque
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

#SW문제와 달리 test case가 몇 개인지 모른다. 동적으로 하기 위해 while True를 사용
while True:
    W, H = map(int, input().split())
    #마지막 case 중 0, 0 인 경우를 위하여 추가함
    if W==0 and H==0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    Icnt = 0 #섬 개수

    chk = [[1]*W for _ in range(H)] #방문했는지 파악용 배열 (0이면 섬이거나, 방문했거나)
    q = deque()

    for i in range(H):
        for j in range(W):
            if arr[i][j]==0:
                chk[i][j]=0


    for i in range(H):
        for j in range(W):
            if chk[i][j]==1:
                Icnt +=1
                q.append([i, j]) 
                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        #H, W --> nx, ny 헷갈려서 list index 에러 많이 났다 ㅎ.ㅎ 시펄...
                        if 0 <= nx < H and 0 <= ny < W and chk[nx][ny]:
                            q.append([nx, ny])
                            chk[nx][ny]=0
    print(Icnt)
                