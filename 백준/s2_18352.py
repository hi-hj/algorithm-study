import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
answer = [-1] * (n+1)
answer[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if answer[nxt] == -1:
            answer[nxt] = answer[now] + 1
            queue.append(nxt)

for i in range(n+1):
    if answer[i] == k:
        print(i)
if k not in answer:
    print(-1)