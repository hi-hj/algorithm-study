from collections import defaultdict
import copy
from heapq import heappop, heappush

INF = int(1e9)



def reverse(graph, trap):
    trap_go = copy.deepcopy(graph[trap])
    for key, val in graph.items():
        # A --> Trap
        for go, cost in graph[key]:
            if go == trap:
                graph[trap].append([key, cost])
                graph[key].remove([trap, cost])
    # Trap --> A
    for go, cost in trap_go:
        graph[trap].remove([go, cost])
        graph[go].append([trap, cost])
    return graph



def solution(n, start, end, roads, traps):
    graph = defaultdict(list)
    for p,q,s in roads:
        graph[p].append([q,s])

    table = [INF for i in range(n+1)]
    table[start] = 0
    table[0] = -1
    pq = [[0,start, graph]]
    # 다익스트라
    while pq:
        cost, now, now_graph = heappop(pq)
        if now in traps:
            now_graph = reverse(now_graph, now)
        
        if table[now] < cost: continue
        
        for item in now_graph[now]:
            nx, ncost = item[0], item[1]
            ncost += cost
            if ncost < table[nx] or table[end]==INF:
                table[nx] = ncost
                heappush(pq, [ncost, nx, now_graph])
    print(table)
    return table[end]
                

solution(3,1,3,[[1, 2, 2], [3, 2, 3]], [2])
solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3])