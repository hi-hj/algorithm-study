import sys
import heapq
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# print(graph)



def dijkstra(graph, start):

    max_num = 0

    distances = [sys.maxsize]*(n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        weight, now = heapq.heappop(queue)
        
        if distances[now] < weight:
            continue
        
        for new_dest, new_weight in graph[now]:
            cost = weight + new_weight
            if cost < distances[new_dest]:
                distances[new_dest] = cost
                heapq.heappush(queue, (cost, new_dest))
                max_num = max(max_num, new_weight)
    
    print(distances)
    print(max_num)
dijkstra(graph, 1)


    