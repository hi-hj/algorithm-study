import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())

kevin = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    kevin[a].append(b)
    kevin[b].append(a)

results = []

def bfs(start):
    queue = collections.deque()
    cnt = 1
    queue.append((start, cnt))
    result = [0 for _ in range(n+1)]
    result[start] = cnt

    while queue:
        now, cnt = queue.popleft()
        for i in kevin[now]:
            if result[i]==0:
                result[i] = cnt+1
                queue.append((i, cnt+1))
    
    return sum(result)

for i in range(n):
    r = bfs(i+1)
    results.append(r)


print(results.index(min(results))+1)

