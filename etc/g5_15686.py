def dfs(idx, cnt):
    global ans
    if idx > len(Chicken): #1. 치킨 집 수를 넘으면 종료
        return
    if cnt == M: #2. 치킨 집 수가  M개면 계산 함수 실행 + 종료
        s = 0
        for hx, hy in Home:
            d = 9999
            for j in v:
                cx, cy = Chicken[j]
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans, s) #DFS 최종값 중 가장 작은 것을 선택
                
        return
    #지역 변수(리스트)에 넣고 뺄 때는 이 순서로 하도록 하자.
    #아직 이해가 잘 안된다. 다시 짚어보기
    v.append(idx)
    dfs(idx+1, cnt+1)
    v.pop()
    dfs(idx+1, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 99999
Chicken = []
Home = []
v = [] #
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            Chicken.append((i,j))
        elif arr[i][j]==1:
            Home.append((i,j))
        
dfs(0,0)
print(ans)