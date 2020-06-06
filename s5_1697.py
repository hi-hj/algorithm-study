def dfs(cnt, now, brother):
    global MIN

    if cnt > MIN:
        return
    if now==brother:
        if cnt < MIN:
            MIN = cnt
        return

    dfs(cnt+1, now*2, brother)
    dfs(cnt+1, now+1, brother)
    dfs(cnt+1, now-1, brother)

N, K = map(int, input().split())

if N<K:
    MIN = K-N
    dfs(0, N, K)
else:
    MIN = N-K
    
print(MIN)