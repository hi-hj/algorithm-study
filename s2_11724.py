import sys
input= sys.stdin.readline
import collections
n, m = map(int, input().split())


graph = collections.defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


queue = collections.deque()
visited =[]
cnt = 0

for i in range(1, n+1):
    if i not in visited:
        visited.append(i)
        queue.append(i)
        cnt +=1
        while queue:
            v = queue.popleft()
            for j in graph[v]:
                if j not in visited:
                    visited.append(j)
                    queue.append(j)
print(cnt)


