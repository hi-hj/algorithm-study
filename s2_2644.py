# BFS : 그래프를 hieracrchy 하게만 생각했다...
## 한 점을 기준으로 위, 아래 모두 갈 수 있음

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

visit = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


#print(graph)
def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start]=1

    while queue:
        d = queue.popleft()

        for i in graph[d]:
            if visit[i]==0:
                queue.append(i)
                result[i] = result[d] + 1
                visit[i] =1


bfs(a)

print(result[b] if result[b] != 0 else -1)