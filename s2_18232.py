import sys
input = sys.stdin.readline

import collections


n, m = map(int, input().split())
s, e = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


queue = collections.deque()
queue.append((s,0))
visited = [s]

while queue:
    v, cnt = queue.popleft()
    if v==e:
        break

    calc = [v-1, v+1]
    for i in calc:
        if 0<i<n+1 and i not in visited:
            queue.append((i, cnt+1))
            visited.append(i)

    for i in graph[v]:
        if i not in visited:
            queue.append((i, cnt+1))
            visited.append(i)

print(cnt)